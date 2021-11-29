#!/bin/sh

until cd /usr/src/app/api/
do
    echo "Waiting for server volume..."
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 3
done

gunicorn django_rest_polls.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 1 --log-level debug
