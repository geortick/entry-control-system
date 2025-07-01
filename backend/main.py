# backend/main.py
from fastapi import FastAPI, File, UploadFile, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from typing import List
import face_recognition
import numpy as np
import io
import os
from datetime import datetime
import hashlib

# --- Database Connection ---
# Inside a pod, containers can reach each other on localhost.
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo_user:mongo_pass@localhost:27017")
client = MongoClient(MONGO_URI)
db = client.entry_control_db
people_collection = db.people
admin_collection = db.admin_users

app = FastAPI(title="Entry Control API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Helper Functions ---

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password: str, provided_password: str) -> bool:
    return stored_password == hash_password(provided_password)

def create_initial_admin():
    if admin_collection.count_documents({}) == 0:
        print("Adding initial admin user...")
        admin_collection.insert_one({
            "username": "admin",
            "password": hash_password("admin")
        })

create_initial_admin()

def load_known_faces_from_db():
    """Loads all face embeddings and names from the MongoDB."""
    known_face_encodings = []
    known_face_names = []
    for person in people_collection.find({}, {"name": 1, "face_embeddings": 1}):
        for embedding in person.get("face_embeddings", []):
            known_face_encodings.append(embedding)
            known_face_names.append(person["name"])
    return known_face_encodings, known_face_names

@app.post("/register/")
async def register(
    name: str = Body(...),
    user_type: str = Body("Authorized"),
    rut: str = Body(None),
    motive: str = Body(None),
    file: UploadFile = File(...)
):
    """Registers a new person (Authorized or Visitant) in the database."""
    contents = await file.read()
    image = face_recognition.load_image_file(io.BytesIO(contents))
    face_encodings = face_recognition.face_encodings(image)
    
    if len(face_encodings) == 0:
        return {"status": "error", "message": "No se encontró rostro."}

    embedding = face_encodings[0].tolist()

    person_doc = {
        "name": name,
        "user_type": user_type,
        "created_at": datetime.utcnow(),
        "face_embeddings": [embedding]
    }
    
    # Add RUT and motive if provided (for visitors)
    if rut:
        person_doc["rut"] = rut
    if motive:
        person_doc["motive"] = motive
    
    people_collection.insert_one(person_doc)
    return {"status": "success", "message": f"{user_type} '{name}' registrado."}

@app.post("/recognize/")
async def recognize(file: UploadFile = File(...)):
    """Recognizes a face against the database."""
    contents = await file.read()
    unknown_image = face_recognition.load_image_file(io.BytesIO(contents))
    
    # Get face locations and encodings
    face_locations = face_recognition.face_locations(unknown_image)
    unknown_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    # First check if ANY face is detected
    if not unknown_encodings or not face_locations:
        return {"status": "success", "result": "No face detected", "message": "No se detectó ningún rostro"}

    # A face was detected! Now get face coordinates
    face_location = face_locations[0]  # (top, right, bottom, left)
    top, right, bottom, left = face_location
    face_coords = {
        "top": int(top),
        "right": int(right), 
        "bottom": int(bottom),
        "left": int(left),
        "width": int(right - left),
        "height": int(bottom - top)
    }
    
    # Now check if we have registered users to compare against
    known_encodings, known_names = load_known_faces_from_db()
    
    if not known_encodings:
        # Face detected but no registered users in database
        return {
            "status": "success", 
            "result": "Not recognized",
            "message": "Rostro detectado pero no hay usuarios registrados",
            "face_coords": face_coords
        }
    
    # Use the first detected face for comparison
    unknown_encoding = unknown_encodings[0]
    
    # Compare against known faces
    matches = face_recognition.compare_faces(known_encodings, unknown_encoding, tolerance=0.6)
    name = None
    user_type = None
    motive = None
    rut = None
    
    face_distances = face_recognition.face_distance(known_encodings, unknown_encoding)
    if len(face_distances) > 0:
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]
            # Get full user data from database including motive
            user_data = people_collection.find_one({"name": name})
            if user_data:
                user_type = user_data.get("user_type", "Unknown")
                motive = user_data.get("motive", None)
                rut = user_data.get("rut", None)
    
    if name:
        response = {
            "status": "success", 
            "result": "Recognized", 
            "name": name,
            "user_type": user_type,
            "face_coords": face_coords,
            "message": f"Usuario reconocido: {name}"
        }
        
        # Add motive and RUT if available (for personalized greetings)
        if motive:
            response["motive"] = motive
        if rut:
            response["rut"] = rut
            
        return response
    else:
        return {
            "status": "success", 
            "result": "Not recognized",
            "message": "Rostro detectado pero no reconocido en la base de datos",
            "face_coords": face_coords
        }

@app.post("/admin/login/")
async def admin_login(
    username: str = Body(...),
    password: str = Body(...)
):
    """Admin authentication endpoint."""
    admin = admin_collection.find_one({"username": username})
    
    if not admin or not verify_password(admin["password"], password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    return {"status": "success", "message": "Inicio de sesión exitoso"}

@app.get("/admin/users/")
async def get_all_users():
    """Get list of all registered users."""
    users = []
    for person in people_collection.find():
        user_data = {
            "id": str(person["_id"]),
            "name": person["name"],
            "user_type": person["user_type"],
            "created_at": person["created_at"].isoformat(),
            "face_count": len(person.get("face_embeddings", []))
        }
        
        # Add RUT and motive for visitors
        if person.get("rut"):
            user_data["rut"] = person["rut"]
        if person.get("motive"):
            user_data["motive"] = person["motive"]
            
        users.append(user_data)
    return {"status": "success", "users": users}

@app.delete("/admin/users/{user_id}")
async def delete_user(user_id: str):
    """Delete a user by ID."""
    from bson import ObjectId
    
    try:
        result = people_collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 1:
            return {"status": "success", "message": "Usuario eliminado exitosamente"}
        else:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    except Exception as e:
        raise HTTPException(status_code=400, detail="ID de usuario inválido")
