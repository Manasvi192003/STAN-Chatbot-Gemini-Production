from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def call_llm(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="models/gemini-1.0-pro",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print("Gemini error:", e)
        return "Hmm… I need a moment. Let’s try again 🙂"


