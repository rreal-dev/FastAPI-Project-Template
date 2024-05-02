# /app/auth/deps.py
from fastapi import HTTPException, Depends, Request, status

def get_current_user(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return user

