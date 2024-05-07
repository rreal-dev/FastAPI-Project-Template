from pydantic import BaseModel

class AssistantCreate(BaseModel):
    name: str
    description: str

class AssistantDisplay(BaseModel):
    id: str
    name: str
    description: str
