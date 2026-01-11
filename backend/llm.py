import os
import requests
from google import genai
from google.genai.errors import ClientError
from config import GEMINI_API_KEY

# Initialize Gemini ONLY if key exists
gemini_client = None
if GEMINI_API_KEY:
    gemini_client = genai.Client(api_key=GEMINI_API_KEY)

def call_gemini(prompt: str) -> str:
    if not gemini_client:
        return "Hmm… I’m having trouble responding right now."

    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        print("Gemini error:", e)
        return "Hmm… I need a moment. Let’s try again 🙂"


def call_llm(prompt: str) -> str:
    # ONLY Gemini (no Ollama now)
    return call_gemini(prompt)
