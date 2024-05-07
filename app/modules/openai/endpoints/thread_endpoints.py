from fastapi import APIRouter
from app.modules.openai.services.thread_service import create_thread, add_message_to_thread
from app.modules.openai.schemas.thread_schemas import ThreadCreate, MessageCreate, MessageDisplay

router = APIRouter()

@router.post("/threads", response_model=ThreadCreate)
async def create_thread_endpoint():
    return await create_thread()

@router.post("/threads/{thread_id}/messages", response_model=MessageDisplay)
async def add_message_to_thread_endpoint(thread_id: str, message: MessageCreate):
    return await add_message_to_thread(thread_id, message.content)
