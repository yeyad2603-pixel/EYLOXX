@echo off
title EYLOX Local Server
color 0A
echo.
echo  ============================================
echo   EYLOX  --  Starting local server...
echo  ============================================
echo.

:: Find node.exe — check common install locations
set NODE=
if exist "%ProgramFiles%\nodejs\node.exe"      set NODE="%ProgramFiles%\nodejs\node.exe"
if exist "%ProgramFiles(x86)%\nodejs\node.exe" set NODE="%ProgramFiles(x86)%\nodejs\node.exe"
if exist "%APPDATA%\nvm\current\node.exe"       set NODE="%APPDATA%\nvm\current\node.exe"
if exist "%LOCALAPPDATA%\Programs\nodejs\node.exe" set NODE="%LOCALAPPDATA%\Programs\nodejs\node.exe"

:: Try node from PATH as fallback
if "%NODE%"=="" (
  where node >nul 2>&1
  if not errorlevel 1 set NODE=node
)

if "%NODE%"=="" (
  echo  ERROR: Node.js not found!
  echo.
  echo  Please install Node.js from https://nodejs.org
  echo  (Choose the "LTS" version)
  echo.
  pause
  exit /b 1
)

echo  Node found: %NODE%
echo  Starting server at http://localhost:3000 ...
echo.
echo  Press Ctrl+C to stop the server.
echo.

%NODE% "%~dp0serve.js"

pause