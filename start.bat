@echo off

:: Step 1: Activate the virtual environment (on Windows)
call venv\Scripts\activate

:: Step 2: Run the Python script
python main.py

:: Keep the command prompt open after the script finishes
pause
