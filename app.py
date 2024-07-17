from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return f"X-Forwarded-For: {request.headers.get('X-Forwarded-For')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
