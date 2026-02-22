# Cloud Assignment — Dockerized Flask App

A simple, production-ready Flask web app packaged with Docker as part of the cloud assignment. This repository demonstrates containerizing a Python web service, local development, and basic CI-friendly practices.

## Quick features
- Minimal Flask API with healthcheck and sample endpoints
- Dockerfile for a small, reproducible image
- docker-compose for local development
- .env support for configurable settings
- Basic unit tests (pytest)

## Quick start (Windows)
1. Clone repo and open the folder:
   - cd d:\cloud_assignment
2. Create virtual env (optional):
   - python -m venv .venv
   - .\.venv\Scripts\activate
   - pip install -r requirements.txt
3. Run locally:
   - set FLASK_APP=app.py
   - flask run

## Run with Docker
Build:
- docker build -t cloud-assignment-flask .

Run:
- docker run --rm -p 5000:5000 --env-file .env cloud-assignment-flask

With docker-compose:
- docker-compose up --build

## Endpoints (examples)
- GET /health — returns status
- GET / — simple welcome message
- POST /echo — returns posted JSON

Example:
- curl http://localhost:5000/health

## Testing
- pytest

## Tips
- Use .env to keep secrets out of source control.
- Add a multi-stage Dockerfile to reduce image size.
- Include a CI pipeline step to run tests and build the image.

