#!/bin/sh
# /docker/traefik/generate_cert.sh:

# Generar certificado SSL autofirmado para 0.0.0.0
openssl req -x509 -nodes -newkey rsa:4096 -keyout /etc/traefik/cert.key -out /etc/traefik/cert.crt -days 365 -subj "/CN=0.0.0.0"

# Configurar certificado SSL en Traefik
cat /etc/traefik/cert.crt /etc/traefik/cert.key > /etc/traefik/cert.pem
