from flask import Blueprint, render_template, jsonify
import speedtest
import statistics
import time

# Define the blueprint
speedtest_app = Blueprint('speedtest_app', __name__, template_folder='templates')

# Function to measure jitter with a limited number of pings
def measure_jitter(st, server, num_pings=3):
    pings = []
    for _ in range(num_pings):
        st.get_best_server([server])  # Ensure we're testing the same server
        ping = st.results.ping
        pings.append(ping)
        time.sleep(0.5)  # Small delay between pings to avoid overwhelming the server
    jitter = statistics.stdev(pings) if len(pings) > 1 else None  # Calculate jitter
    return jitter

# Run speed test with performance optimizations
def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()  # Get the best server

    # Run the speed test using multithreading for faster results
    download = st.download(threads=4) / 1e6  # Convert to Mbps
    upload = st.upload(threads=4) / 1e6  # Convert to Mbps
    ping = st.results.ping

    # Measure jitter
    jitter = measure_jitter(st, st.results.server)

    # Collect server info for transparency
    server_info = {
        'name': st.results.server['sponsor'],
        'location': f"{st.results.server['name']}, {st.results.server['country']}",
        'ping': ping,
        'jitter': jitter
    }
    return download, upload, ping, jitter, server_info

# Homepage for the speedtest blueprint
@speedtest_app.route('/')
def index():
    return render_template('speedtest.html')

# API endpoint to start the speed test
@speedtest_app.route('/start-test', methods=['GET'])
def start_test():
    download, upload, ping, jitter, server_info = run_speed_test()
    return jsonify(download=download, upload=upload, ping=ping, jitter=jitter, server_info=server_info)
