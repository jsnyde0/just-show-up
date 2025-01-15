# Pull base image
FROM python:3.12.2-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set work directory called `app`
RUN mkdir -p /app
WORKDIR /app

# Install UV and dependencies
COPY pyproject.toml ./
RUN pip install --upgrade pip && \
    pip install uv && \
    uv pip install --system .

# Copy local project
COPY . /app

# Expose port 8000
EXPOSE 8000


COPY entrypoint.sh ./
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
