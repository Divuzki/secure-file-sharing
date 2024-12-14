from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from encryption import encrypt_file, decrypt_file
import os
import io  # Required for in-memory file handling

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'

# In-memory user store (for simplicity)
users = {}

# User class
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('dashboard.html', files=files)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    if username in users:
        return jsonify({'message': 'User already exists!'}), 400
    users[username] = password
    return redirect(url_for('home'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        user = User(username)
        login_user(user)
        return redirect(url_for('dashboard'))
    return jsonify({'message': 'Invalid credentials!'}), 401

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        encrypt_file(file.read(), filepath)
        return redirect(url_for('dashboard'))
    return jsonify({'message': 'No file uploaded!'}), 400

@app.route('/download/<filename>', methods=['GET'])
@login_required
def download_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        decrypted_data = decrypt_file(filepath)
        return send_file(
            io.BytesIO(decrypted_data),
            as_attachment=True,
            download_name=f"decrypted_{filename}",
            mimetype='application/octet-stream'
        )
    except FileNotFoundError:
        return jsonify({'message': 'File not found'}), 404
    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@app.route('/download-encrypted/<filename>', methods=['GET'])
@login_required
def download_encrypted_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        return send_file(
            filepath,
            as_attachment=True,
            download_name=f"encrypted_{filename}",
            mimetype='application/octet-stream'
        )
    except FileNotFoundError:
        return jsonify({'message': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
