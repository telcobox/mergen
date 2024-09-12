import subprocess
import platform
from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        host = request.form.get('host')
        result = ping_host(host)
    return render_template('ping_latency.html', result=result)

if __name__ == '__main__':
    app.run(port=5004, debug=True)
