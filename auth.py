from flask_login import UserMixin, login_user, logout_user
from flask import jsonify

# In-memory user store
users = {}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

def get_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

def register_user(request):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({'message': 'User already exists!'}), 400
    users[username] = password
    return jsonify({'message': 'User registered successfully!'})

def login_user_func(request):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        user = User(username)
        login_user(user)
        return jsonify({'message': 'Login successful!'})
    return jsonify({'message': 'Invalid credentials!'}), 401

def logout_user_func():
    logout_user()
    return jsonify({'message': 'Logged out successfully!'})
