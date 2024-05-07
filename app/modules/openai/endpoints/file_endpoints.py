from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from app.modules.openai.services.file_service import upload_file_to_openai
from app.modules.openai.schemas.file_schemas import FileUpload, FileDisplay

router = APIRouter()

@router.post("/files/upload", response_model=FileDisplay)
async def upload_file_endpoint(file: UploadFile = File(...)):
    """
    Uploads a file to OpenAI and returns the file details including any ID or URL provided by OpenAI.
    """
    try:
        file_data = await upload_file_to_openai(file)
        return {
            "id": file_data.id,
            "filename": file.filename,
            "url": file_data.url  # Assuming OpenAI API returns a URL for the uploaded file
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/files/{file_id}", response_model=FileDisplay)
async def get_file_details(file_id: str):
    """
    Retrieve details of a specific file by its ID.
    """
    try:
        file_data = await get_file_info(file_id)  # This would be another service function to implement.
        return {
            "id": file_data.id,
            "filename": file_data.filename,
            "url": file_data.url
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File not found: {str(e)}")
