#!/bin/sh

echo "Running app in debug mode. Attach (F5) to make the app start."
exec sh -c "uv run python -m debugpy --wait-for-client --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000"
