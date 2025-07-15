#!/bin/bash

# Detect OS
OS="$(uname -s)"

# Set Python command and venv activate script depending on OS
if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
    PYTHON_CMD=python3
    ACTIVATE_SCRIPT=".venv/bin/activate"
    MENU_PACKAGE="simple-term-menu"
else
    PYTHON_CMD=python
    ACTIVATE_SCRIPT=".venv/Scripts/activate"
    MENU_PACKAGE=""
fi

# Create virtual environment if not already created
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    $PYTHON_CMD -m venv .venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source "$ACTIVATE_SCRIPT"

# Upgrade pip inside the venv
$PYTHON_CMD -m pip install --upgrade pip

# Install dependencies into the venv
$PYTHON_CMD -m pip install colorama art==5.7

# Install simple-term-menu only if Linux or macOS
if [ -n "$MENU_PACKAGE" ]; then
    $PYTHON_CMD -m pip install "$MENU_PACKAGE"
fi

# Run the game
$PYTHON_CMD main.py

# Deactivate the venv when done
deactivate