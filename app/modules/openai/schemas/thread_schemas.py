from pydantic import BaseModel

class ThreadCreate(BaseModel):
    id: str

class MessageCreate(BaseModel):
    content: str

class MessageDisplay(BaseModel):
    id: str
    content: str
