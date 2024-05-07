from fastapi import APIRouter
from app.modules.openai.services.assistant_service import create_assistant, list_assistants
from app.modules.openai.schemas.assistant_schemas import AssistantCreate, AssistantDisplay

router = APIRouter()

@router.post("/assistants", response_model=AssistantDisplay)
async def create_assistant_endpoint(assistant: AssistantCreate):
    return await create_assistant(assistant.name, assistant.description)

@router.get("/assistants", response_model=list[AssistantDisplay])
async def list_assistants_endpoint():
    return await list_assistants()
