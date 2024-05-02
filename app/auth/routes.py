# /app/auth/routes.py:
from fastapi import APIRouter, Request, HTTPException
from starlette.responses import RedirectResponse
from msal import ConfidentialClientApplication
from app.core.config import settings
from app.core.custom_logger import get_logger
from urllib.parse import urlparse, urlunparse

logger = get_logger(__name__)
router = APIRouter()

@router.get("/login", name="login")
async def login(request: Request):
    logger.info("Inicio del proceso de autenticación")
    msal_app = ConfidentialClientApplication(
        settings.azure_ad_client_id,
        authority=settings.azure_ad_instance + settings.azure_ad_tenant_id,
        client_credential=settings.azure_ad_client_secret,
    )

    # Siempre utilizar HTTPS para el URI de redirección hacia /auth/getAToken
    redirect_uri = str(request.url_for("authorized")).replace("http://", "https://")

    logger.info(f"Redirect URI: {redirect_uri}")  # Log the redirect URI

    auth_flow = msal_app.initiate_auth_code_flow(["User.Read"], redirect_uri=redirect_uri)
    request.session["auth_flow"] = auth_flow
    logger.info(f"Redirigiendo a la página de inicio de sesión de Azure AD: {auth_flow['auth_uri']}")
    return RedirectResponse(auth_flow["auth_uri"])

@router.get("/getAToken", name="authorized")
async def authorized(request: Request):
    # Manejo del token y redirección después de la autenticación
    logger.info("Recibiendo el token de Azure AD")
    auth_flow = request.session.get("auth_flow", {})
    if not auth_flow:
        logger.error("Falta el flujo de autenticación en la sesión")
        raise HTTPException(status_code=400, detail="Falta el flujo de autenticación")
    msal_app = ConfidentialClientApplication(
        settings.azure_ad_client_id,
        authority=settings.azure_ad_instance + settings.azure_ad_tenant_id,
        client_credential=settings.azure_ad_client_secret,
    )
    result = msal_app.acquire_token_by_auth_code_flow(auth_flow, dict(request.query_params))
    if "error" in result:
        logger.error(f"Error al adquirir el token de Azure AD: {result.get('error_description')}")
        raise HTTPException(status_code=401, detail=result.get("error_description"))
    request.session["user"] = result.get("id_token_claims")

    # Aquí determinamos el esquema de URI final basado en el entorno
    final_redirect_scheme = "http" if settings.environment == "development" else "https"
    final_redirect_url = str(request.url_for("home_page")).replace("https://", f"{final_redirect_scheme}://")

    logger.info("Usuario autenticado exitosamente, redirigiendo a la página de inicio")
    return RedirectResponse(url=final_redirect_url)

@router.get("/logout", name="logout")
async def logout(request: Request):
    request.session.pop("user", None)
    logger.info("Usuario desconectado, redirigiendo a la página principal")
    return RedirectResponse(url=request.url_for("root"))