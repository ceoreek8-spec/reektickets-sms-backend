from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'SMS Backend',
        'message': 'Flask app working on Vercel'
    })

@app.route("/api/send-sms", methods=["POST"])
def send_sms():
    return jsonify({
        'success': False,
        'message': 'SMS functionality not yet implemented'
    })

@app.route("/", methods=["GET"])
def home():
    return jsonify({'message': 'SMS Backend API'})
