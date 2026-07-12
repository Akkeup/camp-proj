import user

gKey = 2
pKey = 23

Alice = user.User(gKey, pKey, secretKey = 5)
Bob = user.User(gKey, pKey, secretKey = 15)

A = Alice.generate_public_key()
B = Bob.generate_public_key()

# Channel = user.Channel()
# Channel.transport(A, Bob)
# Channel.transport(B, Alice)

# sA = Alice.secret_encrypted_key
# sB = Bob.secret_encrypted_key

# #  ---

# print(f"Alice's public key: {A}")
# print(f"Bob's public key: {B}")

# print(f"Alice's secret key: {sA}")
# print(f"Bob's secret key: {sB}") 

# print("-"*20)

# message = "Привет Боб, я Алиса, как дела?"
# print("Alice encrypted:", message)
# cryptoA = Alice.crypt_message(message, sA)
# print("Alice crypted:", cryptoA)

# Channel.messeging(cryptoA, Bob)

# encrypto = Bob.encrypt_message(cryptoA, sB)
# print("Bob encrypted:", encrypto)

# print("-"*20)

#  ---

HackChannel = user.Mellory(gKey, pKey, MellorySecretKey = 6, Alice=Alice, Bob=Bob)

H = HackChannel.generate_public_key()

HackChannel.transport(A, Bob)
HackChannel.transport(B, Alice)

sA = HackChannel.AliceCryptoKey
sB = HackChannel.BobCryptoKey

print(f"Alice's public key: {A}")
print(f"Bob's public key: {B}")

print(f"Alice's secret key: {sA}")
print(f"Bob's secret key: {sB}") 

# print(sA == HackChannel.AliceCryptoKey)
# print(sB == HackChannel.BobCryptoKey)
# print(sA == sB)

print("-"*20)

message = "Привет Боб, я Алиса, как дела?"
print("Alice encrypto: ", message)
cryptoA = Alice.crypt_message(message, sA)
print("Alice crypto: ", cryptoA)

HackChannel.messeging(cryptoA, Bob)

encrypto = Bob.encrypt_message(Bob.message, sB)
print("Bob encrypto: ", encrypto)

print("-"*20)