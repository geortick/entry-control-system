# 🚀 Quick Start Guide

## For Contributors/Developers

If you want to modify and republish this system:

### Step 1: Build and Push Your Own Images
```bash
# Build the images
cd backend && podman build -t ghcr.io/YOUR_USERNAME/entry-control-backend:1.0 .
cd ../frontend && podman build -t ghcr.io/YOUR_USERNAME/entry-control-frontend:1.0 .

# Login to GitHub Container Registry
podman login ghcr.io

# Push the images
podman push ghcr.io/YOUR_USERNAME/entry-control-backend:1.0
podman push ghcr.io/YOUR_USERNAME/entry-control-frontend:1.0
```

### Step 2: Update the YAML file
Edit `entry-control-system.yaml` to use your image names instead of `ghcr.io/geortick/...`

### Step 3: Test Your Deployment
```bash
# Test that everything works
./test-deployment.sh
```

## For Others Using Your System

### Single Command Deployment
```bash
# Clone and deploy
git clone https://github.com/YOUR_USERNAME/entry-control-system.git
cd entry-control-system
podman play kube entry-control-system.yaml
```

### Access the Application
- **Main Interface**: http://localhost:8080
- **Admin Panel**: http://localhost:8080/admin.html  
- **Credentials**: admin/admin

### Stop the Application
```bash
podman play kube --down entry-control-system.yaml
```

## What You've Created

✅ **Professional Container Setup**
- Declarative Kubernetes YAML deployment
- Self-contained container images on GitHub Container Registry
- Single-command deployment for end users
- Tight integration with GitHub repository

✅ **Complete Facial Recognition System**  
- Spanish interface with camera capture
- Admin panel with user management
- Real-time facial recognition
- White/blue/red theme

✅ **Production-Ready Structure**
- Proper documentation
- Test scripts
- Easy deployment
- Cloud-native architecture

## Next Steps
1. Create GitHub repository
2. Run deployment setup script
3. Test deployment locally
4. Share with others!

🎉 **You now have a professional, shareable facial recognition system!**
