from flask import Flask
import socket
from datetime import datetime
import os
from feature import get_system_info, generate_system_info_html

app = Flask(__name__)


def get_ip_address():
    """Get the IP address with fallback options"""
    try:
        # Try to get the actual IP address by connecting to a remote server
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        try:
            # Fallback to hostname resolution
            hostname = socket.gethostname()
            return socket.gethostbyname(hostname)
        except Exception:
            return "Unable to determine IP"


@app.route("/")
def hello():
    try:
        hostname = socket.gethostname()
        ip_address = get_ip_address()
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""
            <h1>Hello from DevOps!</h1>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>IP Address:</strong> {ip_address}</p>
            <p><strong>Timestamp:</strong> {time_now}</p>
            <hr>
            <p><a href="/system-info">View System Information</a></p>
        """
    except Exception as e:
        return f"""
            <h1>Hello from DevOps!</h1>
            <p><strong>Error:</strong> {str(e)}</p>
            <p><strong>Timestamp:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        """


@app.route("/system-info")
def system_info():
    """Route to display comprehensive system information"""
    try:
        hostname = socket.gethostname()
        ip_address = get_ip_address()
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return generate_system_info_html(hostname, ip_address, time_now)
    except Exception as e:
        return f"""
            <h1>Hello from DevOps!</h1>
            <p><strong>Error:</strong> {str(e)}</p>
            <p><strong>Timestamp:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            <p><a href="/">Back to Home</a></p>
        """


if __name__ == "__main__":
    # Get configuration from environment variables
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5000))

    app.run(host="0.0.0.0", port=port, debug=debug_mode)
