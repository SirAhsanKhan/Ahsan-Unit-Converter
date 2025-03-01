import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCtIAcsUea0WEnfZpu1E-EyS-7AKltoUFU"
)  # Replace with actual API key

models = genai.list_models()
for model in models:
    print(model.name)
