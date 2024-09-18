from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dns-lookup')
def dnslookup():
    return render_template('/mergen/dns-lookup/templates/dns_lookup.html')

@app.route('/ipsubnet-calculator')
def ipsubnetcalculator():
    return render_template('/mergen/ipsubnet-calculator/templates/ip_calculator.html')

@app.route('/ping-latency-checker')
def pinglatencychecker():
    return render_template('/mergen/ping-latency-checker/templates/ping_latency.html')

@app.route('/whats-my-ip')
def whatsmyip():
    return render_template('/mergen/whats-my-ip/templates/whats_my_ip.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)