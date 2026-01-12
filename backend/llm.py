import google.generativeai as genai
from config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def call_gemini(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "Hmm… I’m having trouble responding right now."

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print("Gemini error:", e)
        return "Hmm… I need a moment. Let’s try again 🙂"

def call_llm(prompt: str) -> str:
    return call_gemini(prompt)

