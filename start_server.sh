#!/usr/bin/env bash

celery -A url_shortener worker -l info & celery -A url_shortener beat  & python3 manage.py runserver 0.0.0.0:8000 & rabbitmq-server start