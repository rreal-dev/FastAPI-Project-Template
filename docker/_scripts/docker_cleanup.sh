#!/bin/bash

# Detener todos los contenedores Docker
echo "Deteniendo todos los contenedores..."
docker stop $(docker ps -a -q)

# Eliminar todos los contenedores Docker
echo "Eliminando todos los contenedores..."
docker rm $(docker ps -a -q)

# Eliminar todas las imágenes Docker
echo "Eliminando todas las imágenes..."
docker rmi $(docker images -q)

# Eliminar todas las redes Docker no utilizadas
echo "Limpiando redes no utilizadas..."
docker network prune -f

# Eliminar todos los volúmenes Docker no utilizados
echo "Limpiando volúmenes no utilizados..."
docker volume prune -f

# Limpieza general del sistema Docker
echo "Realizando limpieza general del sistema Docker..."
docker system prune -af

echo "Limpieza completa."
