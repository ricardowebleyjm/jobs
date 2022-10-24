# pull official base image
FROM python:3.9.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add  gcc musl-dev libmagic \
    && apk add --no-cache mariadb-dev \
    && apk add jpeg-dev zlib-dev libjpeg 

# install dependencies
RUN pip install --upgrade pip


RUN pip install --upgrade pip
RUN mkdir -p /src
WORKDIR /src
COPY requirements.txt /src
COPY entrypoint.sh /src/
RUN pip install -r requirements.txt
COPY . /src

EXPOSE 9003
ENTRYPOINT ["sh", "entrypoint.sh"]
