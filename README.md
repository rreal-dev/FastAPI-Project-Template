# FastAPI Project Template

## Descripción

Este repositorio sirve como una plantilla genérica para iniciar rápidamente proyectos basados en FastAPI. Está diseñado para ser flexible, fácil de personalizar y adecuado para una amplia gama de aplicaciones web y APIs. La plantilla incluye configuración básica, ejemplos de modelos, esquemas, y autenticación, así como una estructura de proyecto recomendada.

## Características

- **FastAPI:** Uso del moderno y rápido framework FastAPI.
- **Autenticación:** Ejemplo de implementación de autenticación.
- **Docker:** Plantilla de Docker y docker-compose para desarrollo y producción.
- **CORS:** Configuración básica de CORS para mayor seguridad.
- **Logger:** Configuración de un sistema de logging básico.
- **Variables de Entorno:** Uso de variables de entorno para configuraciones.
- **Dependencias:** `requirements.txt` para la gestión de dependencias.

## Cómo empezar

### Prerrequisitos

- Python 3.8+
- pip
- Docker (opcional)

### Instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/yourusername/FastAPI-Project-Template.git
cd FastAPI-Project-Template
```

2. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

3. **Configura las variables de entorno**

Copia el archivo `.env.example` a `.env` y ajusta las variables según tu entorno.

```bash
cp .env.example .env
```

4. **Ejecuta el proyecto**

```bash
uvicorn app.main:app --reload
```

El servidor debería estar corriendo y accesible en `http://localhost:8000`.

### Uso de Docker (Opcional)

Para construir y ejecutar el proyecto con Docker Compose:

```bash
docker-compose up --build
```

## Estructura del Proyecto

Descripción de la estructura principal del proyecto:

```
/app
    /api             - Endpoints de la API y lógica de negocio.
    /auth            - Autenticación y control de acceso.
    /core            - Configuración y ajustes centrales del proyecto.
    /models          - Modelos de la base de datos.
    /schemas         - Esquemas Pydantic para validación de datos.
    /services        - Lógica de negocio y servicios auxiliares.
    /views           - Rutas y vistas para la interfaz de usuario.
/docker             - Archivos Docker y scripts para despliegues.
/static             - Archivos estáticos como CSS, JavaScript e imágenes.
/templates          - Plantillas HTML para la interfaz de usuario.
```

## Contribuciones

Las contribuciones son lo que hacen a la comunidad de código abierto un lugar increíble para aprender, inspirar y crear. Cualquier contribución que hagas será **muy apreciada**.

1. Haz Fork del proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Haz commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto

Raúl Real - [LinkedIn](https://www.linkedin.com/in/raul-real/) - rrealgo1@gmail.com

URL del Proyecto: [https://github.com/yourusername/FastAPI-Project-Template](https://github.com/yourusername/FastAPI-Project-Template)
