@echo off
REM Setup script for Energy Solutions Django Backend

echo.
echo ========================================
echo Energy Solutions - Backend Setup
echo ========================================
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create migrations
echo Creating database migrations...
python manage.py makemigrations

REM Apply migrations
echo Applying migrations to database...
python manage.py migrate

REM Create superuser
echo.
echo ========================================
echo Creating admin superuser...
echo ========================================
python manage.py createsuperuser

REM Collect static files
echo Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To start the server, run:
echo   venv\Scripts\activate.bat
echo   python manage.py runserver
echo.
echo Admin panel: http://localhost:8000/admin/
echo API endpoints: http://localhost:8000/api/
echo.
pause
