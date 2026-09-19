# Docker Compose Flask Application

This project demonstrates how to run a simple Flask web application using Docker Compose.

## Technologies

* Python
* Flask
* Docker
* Docker Compose

## Project Structure

* `app.py` - Flask web application
* `Dockerfile` - Docker image configuration
* `docker-compose.yml` - Docker Compose configuration
* `requirements.txt` - Python dependencies

## How to Run

Build the Docker image:

```bash
docker-compose build
```

Start the application:

```bash
docker-compose up -d
```

Check the running container:

```bash
docker-compose ps
```

The application is available at:

`http://localhost:5000`

The application displays:

**Hello from Docker Compose!**

## Stop the Application

```bash
docker-compose down
```

