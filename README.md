# Docker Compose Flask Application

This project demonstrates how to run a Flask web application using Docker Compose.

The application includes health monitoring and environment-based configuration.

## Technologies

- Python
- Flask
- Docker
- Docker Compose

## Project Structure

- `app.py` - Flask web application
- `Dockerfile` - Docker image configuration
- `docker-compose.yml` - Docker Compose configuration
- `requirements.txt` - Python dependencies

## Configuration

The application uses environment variables:

- `APP_VERSION` - application version
- `APP_ENV` - application environment

These variables are configured in `docker-compose.yml`.

## How to Run

Build the Docker image:

docker-compose build

Start the application:

docker-compose up -d

Check the container status:

docker-compose ps

The container should have the following status:

Up (healthy)

## API Endpoints

### Main page

GET /

Returns:

Hello from Docker Compose!

### Health check

GET /health

Returns:

{"status":"healthy"}

### Application information

GET /info

Returns information about the application version and environment.

Example:

{"application":"Docker Compose Flask Application","version":"1.0","environment":"docker"}

## Docker Healthcheck

Docker Compose automatically checks the /health endpoint.

The container is considered healthy when the endpoint responds successfully.

## Stop the Application

docker-compose down
