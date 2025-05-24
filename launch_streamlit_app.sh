#!/bin/bash

VENV_DIR=".venv"
APP_SCRIPT="app/main.py"

source "$VENV_DIR/bin/activate"

# Run the Streamlit app
streamlit run "$APP_SCRIPT"