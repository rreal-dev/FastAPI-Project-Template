# /app/api/endpoints/openai_threads.py
from fastapi import APIRouter, HTTPException, Depends
from app.services.thread_service import ThreadService
from fastapi import Path, Query  # Importar Path y Query para validaciones

router = APIRouter()

@router.post("/threads/start")
async def start_thread():
    try:
        thread = await ThreadService.start_thread()
        return {"thread_id": thread.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create thread: {str(e)}")

@router.post("/threads/{thread_id}/message")
async def send_message(
    thread_id: str = Path(..., description="The ID of the thread to which the message will be added"),
    content: str = Query(..., min_length=1, description="Content of the message"),
    file_id: str = Query(None, description="Optional file ID to attach to the message")
):
    try:
        messages = await ThreadService.send_message(thread_id, content, file_id)
        return {"messages": messages}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")
