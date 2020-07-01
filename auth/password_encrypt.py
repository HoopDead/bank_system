import base64
from Cryptodome.Cipher import AES

class AuthenticationPasswordEncrypter:
    def __init__(self):
        self.secret_key = b"1234567890123456"
    
    def password_encode(self, password):
        cipher = AES.new(self.secret_key,AES.MODE_CTR) # never use ECB in strong systems obviously
        encode = cipher.encrypt(password)
        print(encode)
        return encode

    def password_decode(self, password):
        cipher = AES.new(self.secret_key,AES.MODE_CTR) # never use ECB in strong systems obviously
        decoded = cipher.decrypt(password)
        print(decoded)
        return decoded
