#!/bin/sh

echo "Running app in debug mode"
exec sh -c "uv run python -m debugpy --wait-for-client --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000"
