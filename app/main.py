# /app/main.py:
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.auth.routes import router as auth_router
from app.views import home
from app.core.config import settings
from starlette.middleware.sessions import SessionMiddleware
from app.core.custom_logger import get_logger

from app.api.endpoints.openai_threads import router as threads_router
from app.api.endpoints.openai_assistants import router as assistants_router

logger = get_logger(__name__)

app = FastAPI(title="FastAPI-Project-Template", root_path=f"/{settings.project_name}")

app.add_middleware(SessionMiddleware, secret_key=settings.session_secret_key)

# Configuración para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluye las rutas de autenticación, home, y los nuevos routers de OpenAI
app.include_router(auth_router, prefix="/auth")
app.include_router(home.router)
app.include_router(threads_router, prefix="/api/openai", tags=["OpenAI Threads"])
app.include_router(assistants_router, prefix="/api/openai", tags=["OpenAI Assistants"])


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Llegando solicitud: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Respuesta: {response.status_code} para la ruta {request.url.path}")
    return response

for route in app.routes:
    logger.info(f"Ruta registrada: {route.path}")
