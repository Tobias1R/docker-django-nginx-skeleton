#!/usr/bin/env bash

cd /app/
python3 manage.py migrate
nginx -g "daemon on;"
uwsgi --ini /app/docker/production/web/uwsgi.ini

