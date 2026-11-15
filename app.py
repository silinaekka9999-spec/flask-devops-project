
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask DevOps Project",
        "status": "Success"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "Healthy",
        "application": "Flask API"
    })

@app.route('/api/message')
def message():
    return jsonify({
        "message": "My first DevOps project!"
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
