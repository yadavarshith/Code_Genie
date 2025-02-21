from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
import os

# Initialize FastAPI app
app = FastAPI(title="CodeGenie",
    description="AI-powered code generation API",
    version="1.0.0"
)


# Set up Google Gemini API
GOOGLE_API_KEY = "AIzaSyDmSzyGRf6FoG07ngYIfh7BcrGkIv0QQ2M"  # Replace with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Request model
class CodeRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Welcome to CodeGenie API"}

@app.post("/generate-code/")
@app.post("/generate-code/")
def generate_code(request: CodeRequest):
    try:
        # Use Gemini model to generate code
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(request.prompt)

        # Extract and format the generated code
        generated_code = response.text.strip()

        # Replace `\n` with actual new lines
        formatted_code = generated_code.replace("\\n", "\n")

        return {"generated_code": formatted_code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
