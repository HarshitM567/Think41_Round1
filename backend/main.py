from fastapi import FastAPI
from models import ChatRequest
from database import sessions_col, messages_col
from chat import handle_chat
from uuid import uuid4
from datetime import datetime

app = FastAPI()

@app.post("/api/chat")
async def chat(request: ChatRequest):
    conversation_id = request.conversation_id or str(uuid4())

    user_msg = {
        "user_id": request.user_id,
        "conversation_id": conversation_id,
        "message": request.messages,
        "timestamp": datetime.utcnow(),
        "is_bot": False
    }
    messages_col.insert_one(user_msg)

    ai_response = await handle_chat(request.user_id, conversation_id, request.messages)

    bot_msg = {
        "user_id": request.user_id,
        "conversation_id": conversation_id,
        "message": ai_response,
        "timestamp": datetime.utcnow(),
        "is_bot": True
    }
    messages_col.insert_one(bot_msg)

    return {
        "conversation_id": conversation_id,
        "response": ai_response
    }
