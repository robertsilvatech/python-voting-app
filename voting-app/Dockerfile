FROM python:3.10-slim

COPY requirements.txt requirements.txt
RUN apt update && \
    apt install -y python3-cffi gcc pkg-config g++ libcairo2-dev libicu-dev && \
    apt clean
    
RUN pip install -U pip && pip install pyicu && \
    pip uninstall -y distro-info && \
    pip install -r requirements.txt 

WORKDIR /app
COPY --chmod=777 docker-entrypoint.sh docker-entrypoint.sh
COPY manage.py manage.py
COPY voting_app/ /app/voting_app/

EXPOSE 8000
ENTRYPOINT [ "docker-entrypoint.sh" ]


