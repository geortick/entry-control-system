# Entry Control System

Facial recognition entry control with AI features.

## Setup

1. Create config: `./setup.sh`
2. Edit `.env` with your Gemini API key
3. Deploy: `podman play kube entry-control-system.yaml`

## Access

- Main: http://localhost:8080
- Admin: http://localhost:8080/admin.html (admin/admin)

## Features

- Face recognition for authorized users
- AI-powered visitor registration
- Admin panel for user management
- Security alerts with custom audio

## Security

- API keys in `.env` only (not committed)
- No secrets exposed to frontend
- Clean deployment
