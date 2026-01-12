import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BOT_NAME = "Nova"

if not GEMINI_API_KEY:
    print("⚠️ GEMINI_API_KEY not found. Using fallback.")

