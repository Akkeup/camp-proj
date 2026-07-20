# Bob

import socket

from user import User

HOST = "127.0.0.1"
PORT = 9000

gKey = 2
pKey = 23

Bob = User(gKey, pKey, secretKey=10)
B = Bob.generate_public_key()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    connection, address = server.accept()

    with connection:
        print(f"Connected by {address}")
        connection.sendall(str(B).encode())

        data = connection.recv(1024)
        A = int(data.decode())

        sB = Bob.generate_secret_key(A)  
        print(f"Bob's secret key: {sB}")

        while True:
            data = connection.recv(1024)
            if not data:
                break

            encrypted = Bob.encrypt_message(data, sB)
            print(f"Client: {encrypted}")
            reply = input("Server: ")
            if reply == "exit":
                break

            cryptoReply = Bob.crypt_message(reply, sB)

            connection.sendall(cryptoReply)
