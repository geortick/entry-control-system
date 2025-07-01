# Use a slim Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies needed for opencv and dlib
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a requirements file and install python packages
RUN echo "fastapi" >> requirements.txt && \
    echo "uvicorn" >> requirements.txt && \
    echo "python-multipart" >> requirements.txt && \
    echo "opencv-python-headless" >> requirements.txt && \
    echo "face_recognition" >> requirements.txt && \
    echo "pymongo" >> requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code into the container
COPY ./main.py .

# Expose the port the app runs on
EXPOSE 8000

# The command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
