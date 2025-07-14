# Simple Flask Web App 

A simple web application built using Python's Flask framework.

This is a basic Flask app that displays:
- Hello message
- Hostname and IP address
- Current timestamp

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Environment Variables

- `FLASK_DEBUG`: Set to 'true' to enable debug mode (default: false)
- `PORT`: Port number to run the application (default: 5000)

## Docker

Build and run with Docker:

```bash
docker build -t simple-flask-app .
docker run -p 5000:5000 simple-flask-app
```

