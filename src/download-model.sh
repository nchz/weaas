#!/bin/bash -e

LANG=$1
if [[ -z ${LANG} ]]; then
    echo "First arg must be language (en, es, fr, etc.)"
    exit 1
fi

wget "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.${LANG}.300.bin.gz"
