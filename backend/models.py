from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Message(BaseModel):
    user_id : str
    conversation_id: Optional[str]
    message: str
    timestamp: datetime = datetime.utcnow()
    is_bot: bool = False

class ChatRequest(BaseModel):
    user_id: str
    conversation_id: Optional[str] = None
    messages: str