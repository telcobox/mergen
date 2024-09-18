import subprocess
import platform
from flask import Blueprint, render_template, request

# Create a Blueprint object for the Ping & Latency Checker sub-app
ping_latency_app = Blueprint('ping_latency_app', __name__, template_folder='templates')

# Function to ping a host
def ping_host(host):
    try:
        # Detecting the OS
        if platform.system().lower() == 'windows':
            # Use '-n' for Windows
            ping_command = ['ping', '-n', '4', host]
        else:
            # Use '-c' for Unix-based systems (Linux/Mac)
            ping_command = ['ping', '-c', '4', host]

        output = subprocess.check_output(ping_command, stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output}"

# Define the route for the Ping & Latency Checker
@ping_latency_app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        host = request.form.get('host')
        result = ping_host(host)
    return render_template('ping_latency.html', result=result)
