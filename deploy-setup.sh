#!/bin/bash

# Entry Control System - Deployment Setup Script
# This script helps you push your images to GitHub Container Registry and prepare for deployment

set -e

echo "🚀 Entry Control System - Deployment Setup (GitHub Container Registry)"
echo "====================================================================="

GITHUB_USERNAME="geortick"
BACKEND_IMAGE="ghcr.io/geortick/entry-control-backend:1.0"
FRONTEND_IMAGE="ghcr.io/geortick/entry-control-frontend:1.0"

echo "📋 Configuration:"
echo "   GitHub Username: $GITHUB_USERNAME"
echo "   Backend Image: $BACKEND_IMAGE"
echo "   Frontend Image: $FRONTEND_IMAGE"
echo ""

# Step 1: Login to GitHub Container Registry
echo "🔐 Step 1: Login to GitHub Container Registry"
echo "Please enter your GitHub username and Personal Access Token when prompted..."
echo "💡 Username: Your GitHub username (e.g., $GITHUB_USERNAME)"
echo "💡 Password: Your GitHub Personal Access Token (not your GitHub password!)"
echo "   📝 Create token at: https://github.com/settings/tokens (needs 'write:packages' scope)"
echo ""
podman login ghcr.io

# Step 2: Tag and push backend image
echo ""
echo "🏗️  Step 2: Tagging and pushing backend image..."
podman tag localhost/backend-app:latest "$BACKEND_IMAGE"
echo "Pushing backend image to GitHub Container Registry..."
podman push "$BACKEND_IMAGE"

# Step 3: Tag and push frontend image  
echo ""
echo "🎨 Step 3: Tagging and pushing frontend image..."
podman tag localhost/frontend-app:latest "$FRONTEND_IMAGE"
echo "Pushing frontend image to GitHub Container Registry..."
podman push "$FRONTEND_IMAGE"

# Step 4: Update YAML file
echo ""
echo "📝 Step 4: YAML file already configured for geortick"

echo ""
echo "✅ Setup Complete!"
echo "=================="
echo ""
echo "🎯 Your images are now available on GitHub Container Registry:"
echo "   • $BACKEND_IMAGE"
echo "   • $FRONTEND_IMAGE"
echo ""
echo "🔗 View your packages at: https://github.com/$GITHUB_USERNAME?tab=packages"
echo ""
echo "📁 Your deployment file is ready: entry-control-system.yaml"
echo ""
echo "🚀 To deploy the application:"
echo "   podman play kube entry-control-system.yaml"
echo ""
echo "🌐 Access your application at:"
echo "   • Main Interface: http://localhost:8080"
echo "   • Admin Panel: http://localhost:8080/admin.html"
echo "   • Default credentials: admin/admin"
echo ""
echo "🛑 To stop the application:"
echo "   podman play kube --down entry-control-system.yaml"
echo ""
echo "🎉 Ready to share! Others can now deploy your system with:"
echo "   git clone [your-repo-url]"
echo "   cd entry-control-system"  
echo "   podman play kube entry-control-system.yaml"
