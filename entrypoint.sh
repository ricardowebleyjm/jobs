#!/bin/bash

# Running Database migrations
python manage.py migrate --noinput
#python manage.py collectstatic --noinput --clear



# Running Application with uWSGI
exec gunicorn jobs.wsgi:application \
    --bind=0.0.0.0:9003 \
    --log-level=info \
    --access-logfile=$PWD/accesslog.log \
    --workers=4 \
    --error-logfile=$PWD/errorlog.log \
"$@"