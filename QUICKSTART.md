# 🚀 Quick Start Guide

## For the Project Creator (You)

### Step 1: Push Images to GitHub Container Registry
```bash
# Run the deployment setup script with your GitHub username
./deploy-setup.sh YOUR_GITHUB_USERNAME

# This will:
# 1. Login to GitHub Container Registry (enter your GitHub username and Personal Access Token)
# 2. Tag and push both backend and frontend images
# 3. Update the YAML file with your username
```

**🔑 You'll need a GitHub Personal Access Token:**
- Go to https://github.com/settings/tokens
- Create a new token with `write:packages` permission
- Use your GitHub username and the token (not your password) when prompted

### Step 2: Test Your Deployment
```bash
# Test that everything works
./test-deployment.sh
```

### Step 3: Commit to Git Repository
```bash
git init
git add .
git commit -m "Initial entry control system with camera capture"
git remote add origin https://github.com/YOUR_USERNAME/entry-control-system.git
git push -u origin main
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
