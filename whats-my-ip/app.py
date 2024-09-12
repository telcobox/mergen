from flask import Flask, render_template, request

app = Flask(__name__)

def get_user_ip():
    return request.remote_addr

@app.route('/')
def index():
    user_ip = get_user_ip()
    return render_template('whats_my_ip.html', user_ip=user_ip)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
