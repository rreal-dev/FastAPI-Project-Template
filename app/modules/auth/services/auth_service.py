#/app/modules/auth/services/auth_service.py:
from fastapi import HTTPException, Request
from starlette.responses import RedirectResponse
from msal import ConfidentialClientApplication
from app.core.config import settings
from app.core.custom_logger import get_logger
from app.modules.auth.schemas.auth_schemas import User

logger = get_logger(__name__)

class AuthService:
    @staticmethod
    def _create_msal_app():
        return ConfidentialClientApplication(
            settings.azure_ad_client_id,
            authority=settings.azure_ad_instance + settings.azure_ad_tenant_id,
            client_credential=settings.azure_ad_client_secret,
        )

    @staticmethod
    async def start_login_process(request: Request):
        msal_app = AuthService._create_msal_app()
        redirect_uri = str(request.url_for("authorized")).replace("http://", "https://")
        auth_flow = msal_app.initiate_auth_code_flow(["User.Read"], redirect_uri=redirect_uri)
        request.session["auth_flow"] = auth_flow
        return RedirectResponse(auth_flow["auth_uri"])

    @staticmethod
    async def complete_login_process(request: Request):
        auth_flow = request.session.get("auth_flow", {})
        if not auth_flow:
            raise HTTPException(status_code=400, detail="Authentication flow missing in session.")
        msal_app = AuthService._create_msal_app()
        result = msal_app.acquire_token_by_auth_code_flow(auth_flow, dict(request.query_params))
        if "error" in result:
            raise HTTPException(status_code=401, detail=result.get("error_description"))
        user_data = User(**result.get("id_token_claims"))
        request.session["user"] = user_data.dict()
        final_redirect_url = str(request.url_for("home_page")).replace("https://", "http://")
        return RedirectResponse(url=final_redirect_url)

    @staticmethod
    async def logout_user(request: Request):
        request.session.pop("user", None)
        return RedirectResponse(url=request.url_for("root"))
