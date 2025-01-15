#!/bin/bash

set -e

echo "Starting production deployment process..."

echo "Collecting static files..."
python manage.py collectstatic --noinput || { echo "Static file collection failed"; exit 1; }

echo "Applying database migrations..."
python manage.py migrate --noinput || { echo "Database migration failed"; exit 1; }

echo "Starting Gunicorn..."
exec gunicorn a_core.wsgi:application --bind 0.0.0.0:$PORT
