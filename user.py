import hashlib 

class User:
    def __init__(self, gKey, pKey, secretKey):
        self.gKey = gKey
        self.pKey = pKey
        self.secretKey = secretKey

    def generate_public_key(self):
        self.publicKey = pow(self.gKey, self.secretKey, self.pKey)
        return self.publicKey
    
    def generate_secret_key(self, publicKey):
        self.secret_encrypted_key = pow(publicKey, self.secretKey, self.pKey)
        return self.secret_encrypted_key
    
    def crypt_message(self, message, secret_encrypted_key):
        cryptoKey = hashlib.sha256(str(secret_encrypted_key).encode()).digest()
        message = message.encode()
        crypted_message = bytes([message[i] ^ cryptoKey[i % len(cryptoKey)] for i in range(len(message))])
        return crypted_message

    def encrypt_message(self, message, secret_encrypted_key):
        cryptoKey = hashlib.sha256(str(secret_encrypted_key).encode()).digest()
        decrypted_message = bytes([message[i] ^ cryptoKey[i % len(cryptoKey)] for i in range(len(message))])
        return decrypted_message.decode()
    
    def get_message(self, message):
        self.message = message

class Channel:
    def transport(self, publicKey, recipient):
        recipient.generate_secret_key(publicKey)

    def messeging(self, message, recipient):
        recipient.get_message(message)

class Mellory:
    def __init__(self, gKey, pKey, MellorySecretKey, Alice, Bob):
        self.gKey = gKey
        self.pKey = pKey
        self.MellorySecretKey = MellorySecretKey
        self.Alice = Alice
        self.Bob = Bob

    def generate_public_key(self):
        self.MelloryPublicKey = pow(self.gKey, self.MellorySecretKey, self.pKey)
        return self.MelloryPublicKey
    
    def crypt_message(self, message, secret_encrypted_key):
        cryptoKey = hashlib.sha256(str(secret_encrypted_key).encode()).digest()
        message = message.encode()
        crypted_message = bytes([message[i] ^ cryptoKey[i % len(cryptoKey)] for i in range(len(message))])
        return crypted_message

    def encrypt_message(self, message, secret_encrypted_key):
        cryptoKey = hashlib.sha256(str(secret_encrypted_key).encode()).digest()
        decrypted_message = bytes([message[i] ^ cryptoKey[i % len(cryptoKey)] for i in range(len(message))])
        return decrypted_message.decode()

    def transport(self, publicKey, recipient):
        if recipient is self.Bob:
            self.AliceKey = publicKey
            self.AliceCryptoKey = pow(publicKey, self.MellorySecretKey, self.pKey)
        else:
            self.BobKey = publicKey
            self.BobCryptoKey = pow(publicKey, self.MellorySecretKey, self.pKey)

        recipient.generate_secret_key(self.MelloryPublicKey)

    def messeging(self, message, recipient):
        message = self.encrypt_message(message, self.AliceCryptoKey)
        print("\nMellory's mind: ", message, "\n")
        message = self.crypt_message(message, self.BobCryptoKey)
        recipient.get_message(message)
