# Entry Control System - Sistema de Control de Acceso

A facial recognition-based entry control system with camera capture, user management, and real-time access control.

## 🎯 Features

- **Facial Recognition**: Real-time face detection and recognition using Python
- **Camera Integration**: Direct camera capture for user registration and access control
- **Dual Interface**: Main entry control + Administrative management panel
- **Multi-language**: Spanish interface with English technical documentation
- **User Management**: Register authorized users and visitors
- **Real-time Processing**: Live camera feed with automatic recognition
- **Modern UI**: Clean white/blue/red theme with responsive design

## 🚀 Quick Start (Single Command Deployment)

### Prerequisites
- Podman installed on your system
- Internet connection to pull container images

### Deploy the Application

1. **Clone this repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/entry-control-system.git
   cd entry-control-system
   ```

2. **Deploy with one command**:
   ```bash
   podman play kube entry-control-system.yaml
   ```

3. **Access the application**:
   - **Main Interface**: http://localhost:8080
   - **Admin Panel**: http://localhost:8080/admin.html
   - **Default Admin**: Username: `admin`, Password: `admin`

### Stop the Application
```bash
podman play kube --down entry-control-system.yaml
```

## 📱 Usage

### Main Entry Control Interface
1. Navigate to http://localhost:8080
2. Allow camera access when prompted
3. Position face in frame for automatic recognition
4. System will grant/deny access based on registered users

### Admin Panel
1. Navigate to http://localhost:8080/admin.html
2. Login with admin credentials (admin/admin)
3. **Register New Users**:
   - Choose "Tomar Foto" (Take Photo) or "Subir Archivo" (Upload File)
   - Use camera capture for immediate registration
   - Set user type: Authorized or Visitor
4. **Manage Users**: View and delete registered users

## 🛠 Development Setup

### Building from Source

1. **Backend (Python FastAPI)**:
   ```bash
   cd backend/
   podman build -t your-username/entry-control-backend:1.0 .
   ```

2. **Frontend (Nginx + Static Files)**:
   ```bash
   cd frontend/
   podman build -t your-username/entry-control-frontend:1.0 .
   ```

3. **Push to GitHub Container Registry** (for sharing):
   ```bash
   podman login ghcr.io
   podman push ghcr.io/your-username/entry-control-backend:1.0
   podman push ghcr.io/your-username/entry-control-frontend:1.0
   ```

4. **Update YAML file** with your image names in `entry-control-system.yaml`

### Manual Pod Creation
```bash
# Create pod
podman pod create --name entry-control-pod -p 8080:80 -p 8000:8000

# Run containers
podman run -d --pod entry-control-pod --name mongo-db \
  -e MONGO_INITDB_ROOT_USERNAME=mongo_user \
  -e MONGO_INITDB_ROOT_PASSWORD=mongo_pass \
  mongo:latest

podman run -d --pod entry-control-pod --name backend \
  -e MONGO_URI="mongodb://mongo_user:mongo_pass@localhost:27017" \
  ghcr.io/your-username/entry-control-backend:1.0

podman run -d --pod entry-control-pod --name frontend \
  ghcr.io/your-username/entry-control-frontend:1.0
```

## 🏗 Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │    Database     │
│   (Nginx)       │    │   (FastAPI)     │    │   (MongoDB)     │
│   Port 8080     │◄──►│   Port 8000     │◄──►│   Port 27017    │
│                 │    │                 │    │                 │
│ • HTML/CSS/JS   │    │ • Face Recog    │    │ • User Data     │
│ • Camera UI     │    │ • Image Proc    │    │ • Face Embeddings│
│ • Admin Panel   │    │ • REST API      │    │ • Admin Users   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🐳 Container Images

- **Backend**: `ghcr.io/your-username/entry-control-backend:1.0`
  - Python 3.9 + FastAPI + OpenCV + face_recognition
  - Handles facial recognition processing
  - REST API for registration and authentication

- **Frontend**: `ghcr.io/your-username/entry-control-frontend:1.0`
  - Nginx Alpine + Static HTML/CSS/JS
  - Spanish interface with camera integration
  - Admin management panel

- **Database**: `mongo:latest`
  - MongoDB for user data and face embeddings
  - Persistent storage for all application data

## 🔧 Configuration

### Environment Variables
- `MONGO_URI`: MongoDB connection string
- `MONGO_INITDB_ROOT_USERNAME`: Database admin username
- `MONGO_INITDB_ROOT_PASSWORD`: Database admin password

### Default Credentials
- **Admin Panel**: admin/admin
- **Database**: mongo_user/mongo_pass

## 📋 API Endpoints

- `POST /register/` - Register new user with photo
- `POST /recognize/` - Recognize face from camera
- `POST /admin/login/` - Admin authentication
- `GET /admin/users/` - List all users
- `DELETE /admin/users/{id}` - Delete user

## 🔒 Security Notes

⚠️ **Important**: This is a development setup. For production use:
- Change default passwords
- Use secure MongoDB authentication
- Implement HTTPS
- Add proper user session management
- Consider using secrets management

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🛠 Technologies

- **Backend**: Python, FastAPI, OpenCV, face_recognition, PyMongo
- **Frontend**: HTML5, CSS3, JavaScript, Canvas API, WebRTC
- **Database**: MongoDB
- **Containers**: Podman/Docker
- **Orchestration**: Kubernetes YAML

## 📞 Support

For issues and questions:
1. Check existing GitHub issues
2. Create new issue with detailed description
3. Include system information and error logs
