#!/bin/bash -e

docker run -d \
    --name weaas_nginx \
    -v `pwd`/sockets/:/weaas/sockets/ \
    -v `pwd`/src/nginx.conf:/etc/nginx/nginx.conf \
    -p 80:80 \
    nginx:1.22.0-alpine
