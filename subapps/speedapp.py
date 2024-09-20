from flask import Blueprint, render_template, jsonify
import speedtest

# Define the blueprint
speedtest_app = Blueprint('speedtest_app', __name__, template_folder='templates')

# Run speed test
def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1e6  # Convert to Mbps
    upload = st.upload() / 1e6  # Convert to Mbps
    ping = st.results.ping
    jitter = st.results.server['latency'] if 'latency' in st.results.server else None
    return download, upload, ping, jitter

# Homepage for the speedtest blueprint
@speedtest_app.route('/')
def index():
    return render_template('speedtest.html')

# API endpoint to start the speed test
@speedtest_app.route('/start-test', methods=['GET'])
def start_test():
    download, upload, ping, jitter = run_speed_test()
    return jsonify(download=download, upload=upload, ping=ping, jitter=jitter)
