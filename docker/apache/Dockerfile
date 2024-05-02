# /docker/apache/Dockerfile

FROM httpd:2.4

RUN apt-get update \
    && apt-get install -y openssl \
    && rm -rf /var/lib/apt/lists/*

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /usr/local/apache2/conf/server.key \
    -out /usr/local/apache2/conf/server.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=dev.metaengineering.com"

COPY myapp.conf /usr/local/apache2/conf/myapp.conf

RUN echo "Include /usr/local/apache2/conf/myapp.conf" \
    >> /usr/local/apache2/conf/httpd.conf
