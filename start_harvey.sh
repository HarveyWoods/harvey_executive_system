#!/bin/bash

echo "🚀 Starting Harvey Woods Executive System..."

# Step 1: Activate the virtual environment
source venv/bin/activate

# Step 2: Launch the Harvey Dashboard using the correct interpreter
./venv/bin/python -m dashboard.app
