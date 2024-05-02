#/docker/fastapi/Dockerfile:

# Utiliza una imagen base oficial de Python y muestra la versión de Python y pip
FROM python:3.9-slim
RUN python --version
RUN pip --version

# Establece el directorio de trabajo en el contenedor y muestra el directorio de trabajo
WORKDIR /code
RUN pwd

# Copia el archivo de requisitos primero para aprovechar la caché de la capa de Docker
COPY requirements.txt /code/requirements.txt

# Instala las dependencias del proyecto y muestra las dependencias instaladas
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt && pip freeze

# Copia el resto del código fuente del proyecto al contenedor y muestra los archivos copiados
COPY . /code
RUN ls -la /code/*

# Asegúrate de que el directorio 'static' se copie correctamente y muestra el contenido
COPY ./static /code/static
RUN ls -la /code/static/*

# Comando para ejecutar la aplicación usando uvicorn con recarga en caso de cambios para facilitar la depuración
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5555", "--reload", "--log-level", "debug"]
