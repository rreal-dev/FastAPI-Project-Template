from app.modules.openai.client import client
from fastapi import HTTPException, UploadFile

async def upload_file_to_openai(file: UploadFile):
    try:
        response = client.File.create(file=file.file, purpose="answers")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
