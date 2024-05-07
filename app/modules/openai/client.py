from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.openai_api_key)
