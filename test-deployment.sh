#!/bin/bash

# Entry Control System - Test Deployment Script
# This script tests if your Kubernetes YAML deployment works correctly

echo "🧪 Testing Entry Control System Deployment"
echo "=========================================="

# Stop current pod if running
echo "🛑 Stopping any existing deployment..."
podman play kube --down entry-control-system.yaml 2>/dev/null || true
sleep 2

# Start the deployment
echo "🚀 Starting deployment from YAML..."
podman play kube entry-control-system.yaml

# Wait for containers to start
echo "⏳ Waiting for containers to start..."
sleep 10

# Check pod status
echo "📊 Checking pod status..."
podman pod ps

echo ""
echo "📊 Checking container status..."
podman ps --pod | grep entry-control

# Test connectivity
echo ""
echo "🌐 Testing connectivity..."

# Test frontend
if curl -s --max-time 5 http://localhost:8080 > /dev/null; then
    echo "✅ Frontend is accessible at http://localhost:8080"
else
    echo "❌ Frontend is not responding"
fi

# Test admin page
if curl -s --max-time 5 http://localhost:8080/admin.html > /dev/null; then
    echo "✅ Admin panel is accessible at http://localhost:8080/admin.html"
else
    echo "❌ Admin panel is not responding"
fi

# Test backend (might take longer to start)
echo "⏳ Testing backend API (may take a moment to start)..."
sleep 5

if curl -s --max-time 10 http://localhost:8000/admin/users/ > /dev/null; then
    echo "✅ Backend API is responding at http://localhost:8000"
else
    echo "⚠️  Backend API not responding yet (this is normal, it may need more time)"
fi

echo ""
echo "🎉 Deployment test complete!"
echo "=========================="
echo ""
echo "🌐 Access your application:"
echo "   • Main Interface: http://localhost:8080"
echo "   • Admin Panel: http://localhost:8080/admin.html"
echo "   • Default credentials: admin/admin"
echo ""
echo "📊 Monitor with: podman pod ps"
echo "🛑 Stop with: podman play kube --down entry-control-system.yaml"
