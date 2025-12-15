#!/bin/bash

# Quick start script for Energy Solutions Backend

echo ""
echo "========================================"
echo "Energy Solutions Backend Server"
echo "========================================"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found!"
    echo "Please run setup.sh first"
    echo ""
    exit 1
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Starting Django development server..."
echo ""
echo "========================================"
echo "Backend running at: http://localhost:8000"
echo "Admin panel: http://localhost:8000/admin/"
echo "API: http://localhost:8000/api/"
echo "========================================"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver
