from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from db import save_message, get_last_messages
from memory import store_memory, retrieve_memory
from prompt import build_prompt
from llm import call_llm

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    user_id: str
    message: str

# Guard keywords for hallucination-prone topics
WEATHER_KEYWORDS = [
    "weather", "temperature", "rain", "sunny",
    "cloudy", "forecast", "hot", "cold"
]
@app.post("/chat")
def chat(req: ChatRequest):
    try:
        user_message = req.message.strip()

        # ==============================
        # 1️⃣ HARD SAFETY: WEATHER GUARD
        # ==============================
        if any(word in user_message.lower() for word in WEATHER_KEYWORDS):
            reply = (
                "Hmm… I don’t have a way to see the actual weather where you are. "
                "What’s it like outside for you today?"
            )

            save_message(req.user_id, "user", user_message)
            save_message(req.user_id, "assistant", reply)

            return {"reply": reply}

        # ==============================
        # 2️⃣ LOAD CONTEXT
        # ==============================
        history = get_last_messages(req.user_id)
        memories = retrieve_memory(req.user_id, user_message)

        # ==============================
        # 3️⃣ BUILD PROMPT & CALL MODEL
        # ==============================
        prompt = build_prompt(
            user_message=user_message,
            memories=memories,
            history=history
        )

        reply = call_llm(prompt)

        # ==============================
        # 4️⃣ SAVE CHAT HISTORY
        # ==============================
        save_message(req.user_id, "user", user_message)
        save_message(req.user_id, "assistant", reply)

        # ==============================
        # 5️⃣ STORE LONG-TERM MEMORY
        # ==============================
        if any(
            word in user_message.lower()
            for word in ["like", "love", "enjoy", "favorite", "prefer"]
        ):
            store_memory(req.user_id, user_message)

        return {"reply": reply}

    except Exception as e:
        print("Chat error:", e)
        return JSONResponse(
            status_code=200,
            content={
                "reply": "Hmm… something hiccupped on my end. Let’s try again 🙂"
            }
        )


