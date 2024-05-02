#/docker/traefik/Dockerfile:

# Utiliza una imagen base oficial de Traefik
FROM traefik:v2.5

# Instalar openssl
RUN apk add --no-cache openssl

# Copia el archivo de configuración de Traefik y los scripts al contenedor
COPY ./docker/traefik/traefik.yml /etc/traefik/traefik.yml
COPY ./docker/traefik/generate_cert.sh /etc/traefik/generate_cert.sh
COPY ./docker/traefik/fix-permissions.sh /etc/traefik/fix-permissions.sh

# Cambiar permisos para los scripts
RUN chmod +x /etc/traefik/generate_cert.sh
RUN chmod +x /etc/traefik/fix-permissions.sh

# Ejecutar el script de generación de certificados
RUN /etc/traefik/generate_cert.sh

# Ejecutar Traefik como el punto de entrada y correr el script de permisos justo antes
ENTRYPOINT ["/etc/traefik/fix-permissions.sh" && "/entrypoint.sh"]
