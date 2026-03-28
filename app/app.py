from flask import Flask, request, jsonify

app = Flask(__name__)

# Intentionally vulnerable code for scanning demonstration
SECRET_KEY = "hardcoded-secret-123"  # Bandit will flag this
DEBUG_MODE = True                     # Bandit will flag this

@app.route("/")
def home():
    return jsonify({
        "message": "DevSecOps Demo App",
        "version": "1.0.0",
        "status": "running"
    })

@app.route("/user")
def get_user():
    username = request.args.get("username", "guest")
    return jsonify({
        "user": username,
        "role": "viewer"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=DEBUG_MODE)