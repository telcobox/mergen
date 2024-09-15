from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# ip calculator route - added 1509
@app.route('/ip_calculator')
def ip_calculator():
    return render_template('ip_calculator.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

