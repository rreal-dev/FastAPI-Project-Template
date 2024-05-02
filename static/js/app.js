// Define la URL base para las solicitudes API
const BASE_URL = window.location.origin + "/FastAPI-Project-Template";

// Función para obtener proyectos
async function fetchProjects() {
    const response = await fetch(`${BASE_URL}/projects/`);
    const projects = await response.json();

    const projectsElement = document.getElementById('projects');
    projectsElement.innerHTML = '';
    projects.forEach(project => {
        const projectElement = document.createElement('div');
        projectElement.textContent = project.name;
        projectsElement.appendChild(projectElement);
    });
}

// Llama a la función fetchProjects cuando se carga la página
document.addEventListener('DOMContentLoaded', fetchProjects);
