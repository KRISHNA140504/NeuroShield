#!/bin/bash
echo "Starting NeuroShield Backend Server..."
cd backend
echo "Activating Python environment..."
source neuroshield_env/bin/activate
echo "Starting Flask server..."
python app.py