# /app/api/endpoints/openai_assistants.py
from fastapi import APIRouter, HTTPException
from app.services.assistant_service import create_assistant
from fastapi import Query  # Importar Query para usar en la validación de parámetros

router = APIRouter()

@router.post("/assistants/create")
async def create_openai_assistant(assistant_name: str = Query(..., min_length=3, max_length=50)):
    try:
        assistant_id = await create_assistant(assistant_name, only_if_not_exist=True)
        return {"assistant_id": assistant_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create assistant: {str(e)}")
