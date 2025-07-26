import os
import httpx
from database import products_col

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "mistral-saba-24b"

async def handle_chat(user_id: str, conversation_id: str, user_message: str) -> str:

    prompt = f"""You are a helpful AI assistant. User said: "{user_message}".Search the product
    database if releevant and answer clearly.
    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "messages": [{"role": "user", "content": prompt}],
        "model": GROQ_MODEL
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.groq.com/v1/chat/completions",
            headers=headers,
            json=body
        )
        result = response.json()
        return result["choices"][0]["message"]["content"]