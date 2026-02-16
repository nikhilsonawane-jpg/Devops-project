from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus metric
requests_total = Counter(
    'app_requests_total',
    'Total number of HTTP requests'
)

@app.route('/')
def home():
    requests_total.inc()
    return "DevOps App is Running 🚀"

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

