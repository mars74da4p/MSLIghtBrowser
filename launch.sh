#!/bin/bash
# MSLightBrowser launcher script for Linux

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to project directory
cd "$SCRIPT_DIR"

# Activate virtual environment and run the browser
source .venv/bin/activate
exec python main.py
