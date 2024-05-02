#!/bin/sh
# /docker/traefik/fix-permissions.sh:

# Ajusta los permisos de acme.json
chmod 600 /letsencrypt/acme.json

# Ejecuta el comando original de Traefik
exec "/entrypoint.sh" "$@"
