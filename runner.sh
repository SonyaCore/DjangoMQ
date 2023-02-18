#!/bin/sh
python3 manage.py makemigrations
python3 manage.py makemigrations Inbox Sender
python3 manage.py migrate

if $INIT ; then
   echo "Initial Mode . Creating admin user .."
   python3 manage.py initadmin
fi