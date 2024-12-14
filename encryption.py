from cryptography.fernet import Fernet

# Generate and store your key securely
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(data, filepath):
    encrypted_data = cipher.encrypt(data)
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(filepath):
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    return cipher.decrypt(encrypted_data)
