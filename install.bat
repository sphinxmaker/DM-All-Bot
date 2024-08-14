@echo off

:: Step 1: Check if Python is installed
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python before proceeding.
    pause
    exit /b
)

:: Step 2: Set up a virtual environment (optional but recommended)
python -m venv venv

:: Step 3: Activate the virtual environment (on Windows)
call venv\Scripts\activate

:: Step 4: Install dependencies from requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

echo Installation complete!
pause
