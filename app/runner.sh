#!/bin/sh
python3 consumer.py &
python3 manage.py runserver 0.0.0.0:8080