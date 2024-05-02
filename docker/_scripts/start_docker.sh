#!/bin/bash
# /docker/_scripts/start_docker.sh:

cd ../..

# Función para instalar Docker
install_docker() {
    echo "Docker no está instalado. Iniciando la instalación..."
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce
    echo "Docker ha sido instalado correctamente."
}

# Función para instalar Docker Compose
install_docker_compose() {
    echo "Docker Compose no está instalado. Iniciando la instalación..."
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo "Docker Compose ha sido instalado correctamente."
}

# Verificar si Docker está instalado
docker --version >/dev/null 2>&1
if [ $? -ne 0 ]; then
    install_docker
else
    echo "Docker ya está instalado."
fi

# Verificar si Docker Compose está instalado
which docker-compose >/dev/null 2>&1
if [ $? -ne 0 ]; then
    install_docker_compose
else
    echo "Docker Compose ya está instalado."
fi

# Asegurarse de que el demonio de Docker esté en ejecución
sudo service docker start

# Esperar a que Docker esté listo
while ! docker info >/dev/null 2>&1; do
    echo "Esperando a que Docker esté listo..."
    sleep 1
done

echo "Docker está listo."

# Crear la red traefik si aún no existe
sudo docker network create traefik_public || true

# Iniciar los contenedores utilizando docker-compose
sudo docker-compose up --build --remove-orphans --force-recreate
