# /app/services/thread_service.py
from app.api.openai_manager import create_thread, add_message_to_thread, create_run, get_messages
from fastapi import HTTPException

class ThreadService:
    @staticmethod
    async def start_thread():
        try:
            thread = await create_thread()
            return thread
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to start thread: {str(e)}")

    @staticmethod
    async def send_message(thread_id, content, file_id=None):
        try:
            await add_message_to_thread(thread_id, content, role="user", file_id=file_id)
            run = await create_run(thread_id, assistant_id="your-assistant-id-here")  # Asegúrate de especificar el ID correcto del asistente
            response = await get_messages(thread_id)
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to send message: {str(e)}")
