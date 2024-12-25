from flask import Blueprint, request, jsonify
from models import db, User

user_routes = Blueprint('users', __name__)

@user_routes.route('/', methods=['POST'])
def register_user():
    data = request.json
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@user_routes.route('/', methods=['GET'])
def list_users():
    users = User.query.all()
    user_list = [{"id": user.id, "name": user.name, "email": user.email} for user in users]
    return jsonify(user_list), 200
