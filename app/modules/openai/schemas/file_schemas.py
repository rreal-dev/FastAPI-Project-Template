from pydantic import BaseModel, Field
from typing import Optional

class FileUpload(BaseModel):
    filename: str
    content_type: Optional[str] = None

class FileDisplay(BaseModel):
    id: int
    filename: str
    url: str
