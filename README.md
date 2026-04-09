# SwissTask API

A REST API for task management, built with Flask and PostgreSQL.
Fully containerized with Docker and automated with GitHub Actions CI/CD.

## Tech Stack

- **Backend:** Python / Flask
- **Database:** PostgreSQL 15 + Flask-SQLAlchemy
- **Container:** Docker + Docker Compose (Multi-stage build)
- **CI/CD:** GitHub Actions
- **Testing:** pytest (SQLite in-memory)

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Health check |
| GET | /tasks | List all tasks |
| POST | /tasks | Create a task |
| PUT | /tasks/<id> | Update a task |
| DELETE | /tasks/<id> | Delete a task |

## Quick Start

```bash
make build    # Build Docker image
make up       # Start all services
make down     # Stop all services
make logs     # View logs
Test
bash 
pytest tests/ -v
CI/CD Pipeline
Every push to master:

Runs pytest (7 tests)
Builds Docker image and pushes to Docker Hub
Docker Hub
bash 
docker pull wowmaker/swisstask:latest