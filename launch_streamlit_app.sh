#!/bin/bash

echo "Starting the Streamlit app for Maths Python..."

VENV_DIR=".venv"
APP_SCRIPT="app/maths_python.py"

source "$VENV_DIR/bin/activate"

# Run the Streamlit app
streamlit run "$APP_SCRIPT"