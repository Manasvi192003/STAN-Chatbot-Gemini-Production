import google.generativeai as genai
from config import GEMINI_API_KEY

def call_llm(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "Gemini API key is missing."

    try:
        genai.configure(api_key=GEMINI_API_KEY)

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:
        print("Gemini error:", e)
        return "Hmm… I need a moment. Let’s try again 🙂"


