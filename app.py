from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Docker Compose!"


@app.route("/health")
def health():
    return jsonify(status="healthy")


@app.route("/info")
def info():
    return jsonify(
        application="Docker Compose Flask Application",
        version=os.getenv("APP_VERSION", "1.0"),
        environment=os.getenv("APP_ENV", "docker")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
