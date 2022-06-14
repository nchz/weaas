#!/bin/bash -e

./src/run-nginx.sh
for lang in `ls -1 models/ | cut -d'.' -f1`; do
    ./src/run-app.sh $lang
done
