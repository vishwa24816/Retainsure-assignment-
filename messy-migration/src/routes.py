from flask import Blueprint, request, jsonify
from database import execute_query
from utils import hash_password, check_password

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return "User Management System"

@bp.route('/users', methods=['GET'])
def get_all_users():
    users = execute_query("SELECT id, name, email FROM users")
    return jsonify([dict(user) for user in users])

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = execute_query("SELECT id, name, email FROM users WHERE id = ?", (user_id,), fetchone=True)
    if user:
        return jsonify(dict(user))
    else:
        return jsonify({"error": "User not found"}), 404

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Invalid data"}), 400

    name = data['name']
    email = data['email']
    password = data['password']

    hashed_password = hash_password(password)

    try:
        execute_query("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_password), commit=True)
        return jsonify({"message": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    if not data or ('name' not in data and 'email' not in data):
        return jsonify({"error": "Invalid data"}), 400
    user = execute_query("SELECT * FROM users WHERE id = ?", (user_id,), fetchone=True)
    if not user:
        return jsonify({"error": "User not found"}), 404
    name = data.get('name', user['name'])
    email = data.get('email', user['email'])
    execute_query("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id), commit=True)
    return jsonify({"message": "User updated"})

@bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = execute_query("SELECT * FROM users WHERE id = ?", (user_id,), fetchone=True)
    if not user:
        return jsonify({"error": "User not found"}), 404
    execute_query("DELETE FROM users WHERE id = ?", (user_id,), commit=True)
    return jsonify({"message": "User deleted"})

@bp.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400
    users = execute_query("SELECT id, name, email FROM users WHERE name LIKE ?", ('%' + name + '%',))
    return jsonify([dict(user) for user in users])

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Invalid data"}), 400

    email = data['email']
    password = data['password']
    user = execute_query("SELECT * FROM users WHERE email = ?", (email,), fetchone=True)

    if user and check_password(password, user['password']):
        return jsonify({"status": "success", "user_id": user['id']})
    else:
        return jsonify({"status": "failed"}), 401
