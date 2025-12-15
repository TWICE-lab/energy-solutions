#!/bin/bash

# Setup script for Energy Solutions Django Backend

echo ""
echo "========================================"
echo "Energy Solutions - Backend Setup"
echo "========================================"
echo ""

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create migrations
echo "Creating database migrations..."
python manage.py makemigrations

# Apply migrations
echo "Applying migrations to database..."
python manage.py migrate

# Create superuser
echo ""
echo "========================================"
echo "Creating admin superuser..."
echo "========================================"
python manage.py createsuperuser

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To start the server, run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Admin panel: http://localhost:8000/admin/"
echo "API endpoints: http://localhost:8000/api/"
echo ""
