import user
# import logic

gKey = 2
pKey = 23

Alice = user.User(gKey, pKey, secretKey=5)
Bob = user.User(gKey, pKey, secretKey=15)

A = Alice.generate_public_key()
B = Bob.generate_public_key()

Channel = user.Channel()
Channel.transport(A, Bob)
Channel.transport(B, Alice)

sA = Alice.secret_encrypted_key
sB = Bob.secret_encrypted_key

print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")

print(f"Alice's secret key: {sA}")
print(f"Bob's secret key: {sB}") 

print("-"*20)
# same person
message = "Привет, как дела?"
crypto = Alice.crypt_message(message, sA)
print(crypto)

Channel.messeging(crypto, Bob)

encrypto = Bob.encrypt_message(crypto, sB)
print(encrypto)

print("-"*20)

