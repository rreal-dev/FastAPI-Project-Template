# FastAPI Project Template

## Descripción

Este repositorio sirve como una plantilla robusta y escalable para iniciar proyectos basados en FastAPI, ideal para desarrollo rápido de APIs y aplicaciones web. Con una estructura modular que incluye autenticación avanzada y ejemplos de integración con sistemas externos, esta plantilla está diseñada para facilitar la extensibilidad y mantenimiento.

## Características

- **FastAPI:** Utiliza el moderno y rápido framework FastAPI.
- **Modularidad:** Estructura modular para autenticación, interacción con OpenAI, y más.
- **Autenticación:** Implementación avanzada de autenticación usando MS Azure AD.
- **Docker:** Plantilla de Docker y docker-compose para desarrollo y producción.
- **CORS:** Configuración avanzada de CORS integrada para seguridad mejorada.
- **Logger:** Configuración avanzada de registro de actividades.
- **Variables de Entorno:** Gestión segura de configuraciones a través de variables de entorno.
- **Gestión de Archivos:** Soporte para subida y gestión de archivos con integración de OpenAI.

## Cómo empezar

### Prerrequisitos

- Python 3.8+
- pip
- Docker (opcional)

### Instalación

1. **Clona el repositorio**

```bash
git clone https://github.com/rreal-dev/FastAPI-Project-Template.git
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

Esta sección detalla la estructura principal del proyecto, explicando el propósito de cada directorio y cómo se organizan los módulos:

```
/app
    /modules          - Contiene componentes modulares específicos del proyecto.
        /auth         - Gestiona la autenticación y el control de acceso, incluyendo rutas y servicios necesarios.
        /openai       - Encapsula la integración y manejo de las funcionalidades de OpenAI, como generación de texto y procesamiento de archivos.
    /views           - Alberga las rutas y vistas para la interfaz de usuario, gestionando las respuestas y redirecciones.
    /core            - Incluye configuraciones centrales y utilidades generales del proyecto como configuración del servidor y middleware.
/static             - Almacena archivos estáticos necesarios para la interfaz de usuario, como CSS y JavaScript.
/templates          - Contiene plantillas HTML para renderizar las vistas en el cliente.
/docker             - Incluye Dockerfiles y scripts de docker-compose para facilitar el despliegue y la gestión de contenedores.
```

### Detalle

Cada módulo y directorio está diseñado para ser independiente en la medida de lo posible, permitiendo una fácil extensión y mantenimiento del código. Esta estructura modular ayuda a mantener el proyecto organizado y preparado para escalarse de manera eficiente.

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

URL del Proyecto: [https://github.com/rreal-dev/FastAPI-Project-Template](https://github.com/rreal-dev/FastAPI-Project-Template)
