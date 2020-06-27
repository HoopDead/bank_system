import base64
from Crypto.Cipher import AES

class AuthenticationPasswordEncrypter:
    def __init__(self):
        self.secret_key = "1234567890123456"
    
    def password_encode(self, password):
        cipher = AES.new(self.secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
        encoded = base64.b64encode(cipher.encrypt(msg_text))
        print(encoded)
        return encoded

    def password_decode(self, password):
        cipher = AES.new(self.secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
        decoded = cipher.decrypt(base64.b64decode(encoded))
        print(decoded)
        return decoded
