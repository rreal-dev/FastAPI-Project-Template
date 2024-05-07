from app.modules.openai.client import client
from fastapi import HTTPException

async def create_assistant(name: str, instructions: str):
    try:
        response = client.Assistant.create(name=name, instructions=instructions)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def list_assistants():
    try:
        response = client.Assistant.list()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
