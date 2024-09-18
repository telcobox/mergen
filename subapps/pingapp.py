from ping3 import ping
from flask import Blueprint, render_template, request

# Create a Blueprint object for the Ping & Latency Checker sub-app
ping_latency_app = Blueprint('ping_latency_app', __name__, template_folder='templates')

# Function to ping a host
def ping_host(host):
    try:
        # Perform ping using ping3 library
        response_time = ping(host, timeout=2)  # Timeout is set to 2 seconds
        if response_time is None:
            return f"Ping failed: No response from {host}"
        return f"Response time: {response_time * 1000:.2f} ms"  # Convert seconds to milliseconds
    except Exception as e:
        return f"Ping failed: {str(e)}"

# Define the route for the Ping & Latency Checker
@ping_latency_app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        host = request.form.get('host')
        result = ping_host(host)
    return render_template('ping_latency.html', result=result)
