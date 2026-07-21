# Mellory

import socket

from user import Mellory

HOST = "127.0.0.1"
PORT_1 = 9000
PORT_2 = 9001

gKey = 2
pKey = 23

mellory = Mellory(gKey, pKey, MellorySecretKey=18)
M = mellory.generate_public_key()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as melloryClient:
    melloryClient.connect((HOST, PORT_2))

    data_B = melloryClient.recv(1024)
    B = int(data_B.decode())
   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as melloryServer:
        melloryServer.bind((HOST, PORT_1))
        melloryServer.listen()
        connection, address = melloryServer.accept()

        with connection:
            print(f"Connected by {address}")
            
            data_A = connection.recv(1024)
            A = int(data_A.decode())

            sA = mellory.generate_secret_key(A)
            sB = mellory.generate_secret_key(B)

            connection.sendall(str(M).encode())
            melloryClient.sendall(str(M).encode())

            while True:
                data = connection.recv(1024)
                if not data:
                    break

                decrypted = mellory.encrypt_message(data, sA)
                print(f"Alice (M): {decrypted}")

                encrypted = mellory.crypt_message(decrypted, sB)
                melloryClient.sendall(encrypted)

                data = melloryClient.recv(1024)
                if not data:
                    break
                
                decrypted = mellory.encrypt_message(data, sB)
                print(f"Bob (M): {decrypted}")

                encrypted = mellory.crypt_message(decrypted, sA)
                connection.sendall(encrypted)
