import requests
import time
from google import genai
from google.genai.errors import ClientError
from config import GEMINI_API_KEY

OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"

gemini_client = genai.Client(api_key=GEMINI_API_KEY)


def call_ollama(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
        timeout=60
    )
    response.raise_for_status()
    return response.json()["response"].strip()
def call_gemini(prompt: str) -> str:
    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except ClientError:
        return "Hmm… I need a short moment to recharge. Let’s continue in a bit 💙"

def call_llm(prompt: str) -> str:
    try:
        return call_ollama(prompt)
    except Exception:
        return call_gemini(prompt)


