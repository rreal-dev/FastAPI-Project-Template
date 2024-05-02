# /app/views/home.py:
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from app.auth.deps import get_current_user
from app.core.custom_logger import get_logger
from fastapi.responses import RedirectResponse
from app.core.config import settings

logger = get_logger(__name__)

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", name="root")
async def main_redirect(request: Request):
    user = request.session.get("user")
    logger.info(f"Session User: {user}")  # Log the user from session
    if user:
        redirect_url = request.url_for("home_page")
        logger.info(f"Redirecting authenticated user to: {redirect_url}")
        return RedirectResponse(url=redirect_url)
    else:
        redirect_url = request.url_for("login")
        logger.info(f"Redirecting unauthenticated user to: {redirect_url}")
        return RedirectResponse(url=redirect_url)
    
@router.get("/home", name="home_page")
async def home_page(request: Request, user=Depends(get_current_user)):
    logger.info(f"Usuario {user} accedió a la página de inicio")
    return templates.TemplateResponse("index.html", {"request": request})
