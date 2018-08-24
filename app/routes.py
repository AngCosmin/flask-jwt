from flask import request, jsonify
from app import app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

from app.models import Users

@app.route('/login', methods=['POST'])
def login():
    # if not request.is_json:
    #     return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.form['username']
    password = request.form['password']

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'asd' or password != 'asd':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200