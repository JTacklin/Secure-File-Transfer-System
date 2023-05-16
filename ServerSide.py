import socket
from cryptography.fernet import Fernet

# Function to write key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from the file
def load_key():
    return open("key.key", "rb").read()

# Generate and write a new key
write_key()
key = load_key()

# Create a new socket server
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(f"Server is running on {host}:{port}")

conn, addr = s.accept()
print(f"Received connection from {addr}")

filename = conn.recv(1024).decode("utf-8")
print(f"Receiving {filename}")

with open(filename, 'wb') as file:
    cipher_suite = Fernet(key)
    while True:
        encrypted_data = conn.recv(1024)
        if not encrypted_data:
            break
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        file.write(decrypted_data)

print("File received successfully.")
