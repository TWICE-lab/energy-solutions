@echo off
REM Quick start script for Energy Solutions Backend

title Energy Solutions - Django Backend Server

echo.
echo ========================================
echo Energy Solutions Backend Server
echo ========================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo Virtual environment not found!
    echo Please run setup.bat first
    echo.
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Starting Django development server...
echo.
echo ========================================
echo Backend running at: http://localhost:8000
echo Admin panel: http://localhost:8000/admin/
echo API: http://localhost:8000/api/
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver

pause
