# Alice 

import socket

from user import User

HOST = "127.0.0.1"
PORT = 9000

gKey = 2
pKey = 23

Alice = User(gKey, pKey, secretKey=14)
A = Alice.generate_public_key()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(str(A).encode())
    
    data = client.recv(1024)
    B = int(data.decode())

    sA = Alice.generate_secret_key(B)
    print(f"Alice's secret key: {sA}")

    while True:
        msg = input("Client: ")
        if msg == "exit":
            break
        
        cryptoMsg = Alice.crypt_message(msg, sA)

        client.sendall(cryptoMsg)
        data = client.recv(1024)
        encrypted = Alice.encrypt_message(data, sA)
        print(f"Server: {encrypted}")