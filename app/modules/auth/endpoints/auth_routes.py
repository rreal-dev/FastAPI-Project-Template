#/app/modules/auth/endpoints/auth_routes.py:
from fastapi import APIRouter, Request, HTTPException
from starlette.responses import RedirectResponse
from app.modules.auth.services.auth_service import AuthService
from app.modules.auth.schemas.auth_schemas import TokenData
from app.core.config import settings
from app.core.custom_logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.get("/login", name="login")
async def login(request: Request):
    return await AuthService.start_login_process(request)

@router.get("/getAToken", name="authorized", response_model=TokenData)
async def authorized(request: Request):
    return await AuthService.complete_login_process(request)

@router.get("/logout", name="logout")
async def logout(request: Request):
    return await AuthService.logout_user(request)
