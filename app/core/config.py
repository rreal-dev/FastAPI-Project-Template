# /app/core/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Esto carga las variables de entorno desde un archivo .env
class Settings:
    project_name: str = os.getenv('PROJECT_NAME', 'FastAPI-Project-Template')
    session_secret_key: str = os.getenv('SESSION_SECRET_KEY', 'a_very_secret_key')

    azure_ad_instance: str = os.getenv('AZURE_AD_INSTANCE', 'https://login.microsoftonline.com/')
    azure_ad_tenant_id: str = os.getenv('AZURE_AD_TENANT_ID')
    azure_ad_client_id: str = os.getenv('AZURE_AD_CLIENT_ID')
    azure_ad_client_secret: str = os.getenv('AZURE_AD_CLIENT_SECRET')
    azure_ad_redirect_path: str = f"/{os.getenv('PROJECT_NAME')}/auth/getAToken"

    environment: str = os.getenv('ENVIRONMENT', 'production')

settings = Settings()

