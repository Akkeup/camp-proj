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

class Mellory:
    def __init__(self, gKey, pKey, MellorySecretKey):
        self.gKey = gKey
        self.pKey = pKey
        self.MellorySecretKey = MellorySecretKey

    def generate_public_key(self):
        self.MelloryPublicKey = pow(self.gKey, self.MellorySecretKey, self.pKey)
        return self.MelloryPublicKey
    
    def generate_secret_key(self, publicKey):
        self.secret_encrypted_key = pow(publicKey, self.MellorySecretKey, self.pKey)
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
