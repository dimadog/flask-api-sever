from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from datetime import datetime

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": "secret"
}

@auth.verify_password
def verify_password(login, password):
    if login in users and users[login] == password:
        return login

@app.route('/data', methods=['POST'])
@auth.login_required
def handle_post():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    with open('log.txt','a') as file:
        file.write(datetime.now().strftime("%Y.%m.%d_%H:%M:%S.%f")+str(data)+'\n')
    return jsonify({
        "response": "OK",
        "src-addr": client_ip
    }), 201

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "Unauthorized access"}), 401

if __name__ == '__main__':
    app.run(debug=True)
