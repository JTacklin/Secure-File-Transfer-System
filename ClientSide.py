import socket
from cryptography.fernet import Fernet

# Function to load the key from the file
def load_key():
    return open("key.key", "rb").read()

key = load_key()

# Create a new socket client
s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host, port))

filename = "test.txt"
s.send(filename.encode('utf-8'))

with open(filename, 'rb') as file:
    cipher_suite = Fernet(key)
    while True:
        data = file.read(1024)
        if not data:
            break
        encrypted_data = cipher_suite.encrypt(data)
        s.send(encrypted_data)

print("File sent successfully.")
