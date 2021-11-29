# Django REST Polls

REST API for user polling system.

## Table of content:

* [Contacts](#contacts)
* [Setup with Docker](#contacts)

## Setup with Docker

1. Build and up docker containers:

    ```console
    foo@bar: django-rest-polls $ docker-compose up -d --build
    ```

2. Create superuser:

    ```console
    foo@bar: django-rest-polls$ docker-compose exec api python api/manage.py createsuperuser
    ```

## Contacts:

Created by [@stonedch](https://github.com/stonedch)
