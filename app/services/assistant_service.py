# /app/services/assistant_service.py
from app.api.openai_manager import client
from fastapi import HTTPException

async def create_assistant(assistant_name="DocAssistant", only_if_not_exist=False):
    if only_if_not_exist:
        try:
            existing_assistants = await client.beta.assistants.list()
            for assistant in existing_assistants.data:
                if assistant.name == assistant_name:
                    return assistant.id
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to list assistants: {str(e)}")

    try:
        response = await client.beta.assistants.create(
            name=assistant_name,
            instructions="Eres un asistente especializado en...",
            tools=[{"type": "retrieval"}],
            model="gpt-4-turbo-preview"
        )
        return response.id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create assistant: {str(e)}")
