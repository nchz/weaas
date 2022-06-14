FROM python:3.9-slim

RUN pip install --no-cache-dir \
    flask==2.1.* \
    gensim==4.2.* \
    gunicorn==20.1.*

COPY src/main.py /weaas/
WORKDIR /weaas

RUN echo 'gunicorn -w 1 --bind unix:/weaas/sockets/${LANG} --reload --timeout 300 main:app' > /ep.sh && chmod +x /ep.sh
ENTRYPOINT /ep.sh
