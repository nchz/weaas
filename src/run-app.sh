#!/bin/bash -e

LANG=$1
if [[ -z ${LANG} ]]; then
    echo "First arg must be language (en, es, fr, etc.)"
    exit 1
fi

docker run -d \
    --name weaas_${LANG} \
    -v `pwd`/sockets/:/weaas/sockets/ \
    -v `pwd`/models/:/weaas/models/ \
    -e LANG=${LANG} \
    weaas-app
