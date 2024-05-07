from app.modules.openai.client import client
from fastapi import HTTPException

async def create_thread():
    try:
        thread = client.Thread.create()
        return thread
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def add_message_to_thread(thread_id: str, message_content: str, role: str="user"):
    try:
        message = client.Thread.add_message(thread_id=thread_id, content=message_content, role=role)
        return message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
