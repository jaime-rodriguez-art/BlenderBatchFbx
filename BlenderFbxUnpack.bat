@echo off
setlocal enabledelayedexpansion

cd /

for /f "delims=" %%a in ('dir /b /s blender.exe') do (
    set "blender_executable=%%~dpa"
    goto :found_blender
)

:found_blender
if not exist "!blender_executable!\blender.exe" (
    echo Blender executable not found. Please make sure Blender is installed and accessible.
    exit /b
)

for %%i in ("%~dp0script.py") do set "python_script=%%~fi"

for %%f in ("%~dp0*.blend") do (
    "%blender_executable%\blender.exe" -b "%%~f" -P "%python_script%"
    echo Texture unpacking complete for "%%~nxf"
)
