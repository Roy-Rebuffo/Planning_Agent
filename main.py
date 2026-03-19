# Entry point of the application.
# Run with: streamlit run main.py

import sys
import os

# Add src to the Python path so all modules are found
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from dotenv import load_dotenv
import streamlit as st

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    st.error("❌ GROQ_API_KEY not found. Check your .env file.")
    st.stop()

from ui.streamlit_ui import run_app
run_app()