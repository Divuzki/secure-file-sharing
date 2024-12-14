Secure File Sharing and Monitoring System

Overview

The Secure File Sharing and Monitoring System is a Python-based project designed to provide a secure platform for uploading, storing, and downloading files with encryption and decryption capabilities. This project demonstrates the use of AES symmetric encryption to ensure file confidentiality, integrity, and security. Additionally, it supports user authentication and role-based access control to manage file operations.

Features

Core Functionalities

File Encryption and Upload:

Encrypts files using AES (via the cryptography library).

Stores encrypted files in a secure uploads directory.

Decrypted File Download:

Decrypts files on-the-fly and serves them as plaintext to authorized users.

Encrypted File Download:

Allows users to download the raw encrypted file for secure sharing.

User Authentication:

Supports user registration, login, and logout using Flask-Login.

Dashboard Interface:

A clean and user-friendly dashboard where users can upload files, view files, and download both encrypted and decrypted versions.

Technical Details

Encryption and Decryption

The project uses Fernet encryption from the cryptography library, which provides:

AES encryption in CBC mode with PKCS7 padding.

A secure HMAC for data integrity validation.

Randomized initialization vectors (IVs) for every encryption process.

Code for Encryption:

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(data, filepath):
    encrypted_data = cipher.encrypt(data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

Code for Decryption:

def decrypt_file(filepath):
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    return cipher.decrypt(encrypted_data)

Flask Application Structure

This project uses Flask to provide a RESTful API and a simple front-end dashboard.

Key Components:

main.py:

Handles routes for user authentication, file upload, and file downloads.

Templates:

HTML files (index.html and dashboard.html) for the front-end.

Static Files:

CSS (styles.css) for styling the interface.

JavaScript (scripts.js) for adding interactivity.

Folder Structure

SecureFileSharing/
│
├── main.py               # Main Flask application
├── auth.py               # User authentication logic
├── encryption.py         # Encryption and decryption logic
├── config.py             # Configuration settings
├── uploads/              # Directory for encrypted files
├── templates/            # HTML templates for the front-end
│   ├── index.html        # Login/Register page
│   ├── dashboard.html    # User dashboard for file operations
├── static/               # Static files (CSS, JavaScript)
│   ├── styles.css        # Styling for the front-end
│   ├── scripts.js        # Optional JavaScript interactivity
├── requirements.txt      # Python dependencies
└── README.md             # Documentation

Setup Instructions

Prerequisites

Python 3.9 or higher

Pip (Python package manager)

Installation

Clone the repository:

git clone https://github.com/yourusername/secure-file-sharing.git
cd secure-file-sharing

Create and activate a virtual environment:

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py

Access the app at http://127.0.0.1:5000.

Usage

Upload Files

Log in using your credentials.

Use the dashboard interface to upload files. Uploaded files are encrypted automatically.

Download Files

Decrypted File: Click the "Download Decrypted" button to download the plaintext version.

Encrypted File: Click the "Download Encrypted" button to download the raw encrypted file.

Authentication

Register a new user account.

Login to access the dashboard and manage files.

Logout to securely end the session.

Technical Highlights

AES Encryption: Secures files with industry-standard cryptographic algorithms.

Flask-Login: Simplifies user authentication and session management.

Responsive UI: Provides a clean and intuitive dashboard using HTML/CSS.

Secure Key Management: Uses a generated Fernet key for encryption.

Future Enhancements

Role-Based Access Control: Add roles like "Admin" and "User" for advanced permissions.

Cloud Integration: Integrate with AWS S3 or Azure Blob Storage for scalable file storage.

Audit Logging: Implement detailed logs for user actions and file activity.

Enhanced Key Management: Use secure key storage solutions like AWS Secrets Manager or HashiCorp Vault.

SEO Optimized Keywords

Secure file sharing

AES encryption Python

Flask file upload example

Python file encryption project

Encrypted file sharing application

Flask dashboard example

License

This project is licensed under the MIT License.

Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request. For major changes, open an issue first to discuss what you would like to change.
