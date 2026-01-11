# Nova 🤖 — Emotion-Aware Conversational Companion  
**STAN Internship Challenge Submission**

Nova is a lightweight, emotion-aware conversational companion designed to feel natural, supportive, and human-like — **without ever claiming to be human or explicitly stating it is an AI**.

This project demonstrates:
- Clear separation of **short-term conversation context** and **long-term memory**
- Emotion-sensitive responses
- Realistic assistant behavior (memory persists across sessions)
- Clean frontend experience with typing indicators and timestamps
- Simple, understandable architecture (no overengineering)

---

## ✨ Key Features

### 🧠 Dual-Memory Design (Core Requirement)

Nova uses **two types of memory**, similar to real-world conversational assistants.

#### 1️⃣ Short-Term Memory (Conversation Context)
- Stored in `chat.db`
- Contains only recent messages
- Cleared visually when **New Session** is clicked
- Used to maintain conversational flow

#### 2️⃣ Long-Term Memory (Preferences & Facts)
- Stored in `memory.db`
- Persists across sessions
- Examples:
  - `I like anime`
  - Emotional tendencies
- **NOT cleared on New Session**
- Retrieved using semantic similarity (**FAISS + embeddings**)

✅ This design directly aligns with STAN’s expectations.

---

## 💬 Emotion-Aware Conversations

Nova:
- Responds empathetically to emotional inputs
- Matches the user’s tone
- Never invents memories
- Never claims to be human
- Avoids technical or system explanations in replies

---

## 🖥️ Frontend Highlights

- Clean chat UI (HTML + CSS)
- Typing indicator (`Nova is typing…`)
- Character-by-character message streaming
- Timestamps on every message
- **New Session clears UI only (memory preserved)**

---

## 🏗️ Architecture Overview

```
STAN-Chatbot/
|
|-- backend/
| |-- main.py # FastAPI entry point
| |-- llm.py # LLM routing (Ollama → Gemini fallback)
| |-- prompt.py # Persona & behavior rules
| |-- memory.py # Long-term memory (FAISS + SQLite)
| |-- db.py # Chat history storage
| |-- chat.db # Short-term memory
| |-- memory.db # Long-term memory
|
|-- frontend/
| |-- index.html # Chat UI
|
|-- README.md
|-- requirements.txt

```

---

## ⚙️ Tech Stack

### Backend
- **FastAPI** — API server
- **SQLite** — Lightweight persistent storage
- **Sentence Transformers** — Text embeddings
- **FAISS** — Semantic similarity search
- **Ollama (local)** — Primary LLM
- **Gemini (fallback)** — Cloud backup

### Frontend
- HTML
- CSS
- Vanilla JavaScript

---

## 🚀 How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Start the backend server
```bash
cd backend
python -m uvicorn main:app --reload
```
The backend will start at:
http://127.0.0.1:8000

### 3️⃣ Open the frontend

Open the following file directly in your browser:
```bash
frontend/index.html
```

Example Behaviors
```
| User Input           | Nova’s Behavior                          |
| -------------------- | ---------------------------------------- |
| `I feel low today`   | Responds empathetically                  |
| `I like anime`       | Stored as long-term memory               |
| `New Session`        | UI cleared, memory preserved             |
| `Are you an AI?`     | Identifies as a conversational companion |
| `How is my t-shirt?` | Correctly states limitations             |
| `How’s the weather?` | Avoids claiming real-world sensing       |
```

---

## 🧠 Memory Design

### Short-Term Memory
- Recent messages only  
- Used for conversational continuity  
- Cleared visually on **New Session**

### Long-Term Memory
- User preferences & personal facts  
- Stored in `memory.db`  
- Retrieved via semantic similarity (FAISS)  
- Never fabricated or assumed  

---
## UGC Platform Compatibility

Nova is designed to integrate seamlessly with any user-generated content (UGC) platform.

- Exposes a simple HTTP-based chat API
- Uses user-scoped memory (`user_id`) for safe multi-user environments
- Separates UI sessions from persistent memory
- Persona and behavior are prompt-driven, not platform-specific

This allows Nova to be embedded into web apps, mobile apps, forums, or creator platforms without changes to core logic.


