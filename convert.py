import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def convert_units(value, from_unit, to_unit):
    """
    Uses Gemini LLM to convert between different units.
    """
    prompt = f"Convert {value} {from_unit} to {to_unit}."
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="⚖️", layout="centered")
st.title("Ahsan's Unit Converter")
st.markdown("This app uses Gemini LLM to convert between different units.")

# Custom Styles
st.markdown(
    """
    <style>
        body { background-color: #f8f9fa; }
        .stApp { background: linear-gradient(to right, #ffffff, #ddeeff); color: black; }
        .stTextInput, .stSelectbox, .stNumberInput { background: #ffffff; color: #333; border-radius: 10px; border: 1px solid #ccc; }
    </style>
    """,
    unsafe_allow_html=True,
)
# Input fields
value = st.number_input("Enter value:", min_value=0.0, format="%.6f")
units = [
    "meter", "kilometer", "nanometer", "micrometer", "centimeter", 
     "nautical mile", "mile", "yard", "inch", "foot"
]
from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

if st.button("Convert"):
    if value and from_unit and to_unit:
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} is {result} {to_unit}")
    else:
        st.error("Please enter a value and select units.")

