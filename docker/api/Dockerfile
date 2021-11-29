FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./django_rest_polls/Pipfile /django_rest_polls/Pipfile.lock ./api/

RUN pip install --upgrade pip
RUN pip install pipenv gunicorn

RUN cd ./api/ && pipenv install --system --deploy --ignore-pipfile

COPY ./docker/ ./docker/
COPY ./django_rest_polls/ ./api/
