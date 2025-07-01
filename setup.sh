#!/bin/bash

# Entry Control System - Simple Setup
# Creates .env file with necessary configuration

echo "🚀 Entry Control System Setup"
echo "============================="

# Create .env file
cat > .env << EOF
# Entry Control System Configuration
GEMINI_API_KEY=your_api_key_here
BACKEND_URL=http://127.0.0.1:8000
ENABLE_AI_FEATURES=true
ENABLE_SECURITY_ALERTS=true
EOF

echo "✅ Created .env file"
echo "📝 Edit .env and replace 'your_api_key_here' with your actual Gemini API key"
echo "🔗 Get API key at: https://aistudio.google.com/app/apikey"
echo ""
echo "🚀 To deploy: podman play kube entry-control-system.yaml"
