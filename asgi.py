# asgi.py:
import os
import sys

# Añade el directorio del proyecto al sys.path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Importa la configuración y la aplicación FastAPI
# from app.core.config import settings
from app.main import app as application

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(application, host='0.0.0.0', port=8000)

    # uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="info", root_path=f"/{settings.project_name}")


# uvicorn app.main:app --root-path /FastAPI-Project-Template --reload --host 0.0.0.0 --port 8000 --log-level debug
