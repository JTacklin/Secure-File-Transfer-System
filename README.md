# Secure-File-Transfer-System
The Secure File Transfer System is a Python-based program designed to facilitate secure file transfer over a network. It is divided into two parts: the server and the client. The server is set to listen for incoming connections while the client is designed to initiate a connection with the server for file transfer. Both the server and client leverage Python's built-in socket library for establishing network communication.

For secure data transfer, the system employs Fernet symmetric encryption from the cryptography library. Before the file transfer begins, both the client and the server generate and share a symmetric key. This key is used to encrypt the file data before it's transmitted over the network and then to decrypt it upon receipt. Thus, the transferred file remains secure and intact, protected from any unauthorized access or manipulation during transmission.

<h1>Instructions</h1>

1.Install the cryptography library: Open a terminal or command prompt, and run the following command:


```linux
pip install cryptography
```

2.Save the code: Create two separate Python files, one for the server side (e.g., server.py) and one for the client side (e.g., client.py). Copy the server side code into server.py and the client side code into **client.py**.

3.Prepare a test file: Create a text file (ex: test.txt) with some content in it. Place it in the same directory as the **client.py** script.

4.Run the server: Open a terminal or command prompt, navigate to the directory containing the **server.py** script, and run the following command:

```linux
python server.py
```
The server should now be running and listening for incoming connections.

5.Run the client: In another terminal or command prompt, navigate to the directory containing the client.py script, and run the following command:
```linux
python client.py
```
The client should now connect to the server and send the encrypted test.txt file.

6.Verify the transfer: If the file transfer was successful, you should see a new file with the same name (ex: test.txt) in the server's directory. This file should have the same content as the original file.

<h2>Acknowledgements</h2>

Both the client and the server have the same key for encryption and decryption, which is not typically the case in a secure system. Usually, public key cryptography (asymmetric encryption) is used where the client would encrypt the data with the server's public key, and the server would decrypt it using its private key. This ensures that even if someone intercepts the data, they can't decrypt it without the server's private key.

In a real-world scenario, you would likely use a secure, established protocol like SFTP (SSH File Transfer Protocol) or FTPS (FTP Secure), rather than trying to implement secure file transfer yourself.
