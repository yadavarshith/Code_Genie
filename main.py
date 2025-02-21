from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from fastapi.middleware.cors import CORSMiddleware
import streamlit as st
import requests

# Initialize FastAPI app
app = FastAPI()

# Allow frontend (Streamlit) to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API (Replace with actual API key)
genai.configure(api_key="AIzaSyDmSzyGRf6FoG07ngYIfh7BcrGkIv0QQ2M")

# Request model for input
class CodeRequest(BaseModel):
    prompt: str

@app.post("/generate-code/")
def generate_code(request: CodeRequest):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(request.prompt)
        generated_code = response.text.strip()
        return {"generated_code": generated_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "CodeGenie API is running!"}

# Streamlit UI
def main():
    st.title("CodeGenie - AI-Powered Code Generator")
    prompt = st.text_area("Enter your code prompt:")
    if st.button("Generate Code"):
        if prompt:
            response = requests.post("http://127.0.0.1:8000/generate-code/", json={"prompt": prompt})
            if response.status_code == 200:
                st.code(response.json()["generated_code"], language="python")
            else:
                st.error("Error generating code. Try again.")
        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
