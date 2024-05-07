#/app/modules/auth/schemas/auth_schemas.py:
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., description="The username of the authenticated user")
    email: str = Field(..., description="The email address of the authenticated user")

class TokenData(BaseModel):
    access_token: str = Field(..., description="Access token for API authentication")
    token_type: str = Field(..., description="Type of the token, typically Bearer")
