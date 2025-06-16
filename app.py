from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
        <h1>Hello from DevOps!</h1>
        <p><strong>Hostname:</strong> {hostname}</p>
        <p><strong>IP Address:</strong> {ip_address}</p>
        <p><strong>Timestamp:</strong> {time_now}</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
