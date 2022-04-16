import os

from app import app


@app.route('/')
def index():
    app_name = os.getenv('APP_NAME')

    if app_name:
        return f"Hello from {app_name} runnng in a Docker container Nginx!"

    return "Hello form Flask"
