# Just Show Up

An agentic AI scraping project to learn to work with AI agents.

## Quick Start

### Prerequisites

- Docker, Docker Compose, and `uv` installed on your machine.
- A `.env` file with necessary environment variables (see `.env.example` for reference).

### Setup and Run

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/yourusername/django-starter.git](https://github.com/jsnyde0/just-show-up/)
   cd just-show-up
   ```

2. **Install pre-commit hooks**:
   ```bash
   uv run pre-commit install
   ```

3. **Start the Docker environment for local development**:
   ```bash
   docker compose -f docker-compose.yml -f docker-compose.local.yml up
   ```

   This will automatically apply migrations, create a superuser (if credentials are provided in the `.env` file), and collect static files.

4. **Access the application**:
   - Visit [http://localhost:8000](http://localhost:8000) in your browser.

## Development Workflow

### Running Management Commands

While the entrypoint script handles initial setup tasks, you may need to run other management commands during development:

- **Make Migrations**: After making changes to your models, run:
  ```bash
  docker compose exec app python manage.py makemigrations
  ```

- **Apply Migrations**: To apply new migrations:
  ```bash
  docker compose exec app python manage.py migrate
  ```

- **Create Superuser**: If you need to create a superuser manually:
  ```bash
  docker compose exec app python manage.py createsuperuser
  ```

- **Run Tests**:
  ```bash
  docker compose exec app pytest
  ```

  Or if you want to run without expensive LLM calls:
  ```bash
  docker compose exec app pytest -m "not agentic"
  ```

- **Collect Static Files**:
  ```bash
  docker compose exec app python manage.py collectstatic --noinput
  ```

### Frontend Development

- **Install frontend dependencies**:
  ```bash
  cd node
  npm install
  ```
- **Run Tailwind in watch mode**:
  ```bash
  npm run build
  ```

- **Minify CSS and collect static for production**:
  ```bash
  npm run minify
  cd .. && docker compose exec app python manage.py collectstatic --noinput
  ```

### Debugging

To debug the application with VSCode using Docker Compose:

1. **Start Services in Debug Mode**:
   ```bash
   docker compose -f docker-compose.yml -f docker-compose.debug.yml up --build
   ```

2. **Attach Debuggers in VSCode**:
   - **Django App**: Select 'Attach to App' and press `F5`.
   - **Celery Worker**: Select 'Attach to Celery' and press `F5`.

> **Note**: Both services will wait for the debugger to attach before starting.

This setup allows you to debug both the Django application and the Celery worker effectively.

## Quality Checks

- **Run tests**:
  ```bash
  docker compose exec app pytest
  ```
- **Run code formatting**:
  ```bash
  uv run ruff check .
  uv run ruff format --check .
  ```

## Additional Information

- **Using Flowbite**: Convert Tailwind classes to DaisyUI classes for consistent styling.
- **Environment Variables**: Ensure all necessary environment variables are set in your `.env` file.

## Troubleshooting

- **Database Issues**: Ensure your Docker volumes are set up correctly to persist data.
- **Docker Logs**: Use `docker compose logs` to view logs and troubleshoot issues.
