from base64 import b64encode
from Cryptodome.Cipher import AES
import json

class AuthenticationPasswordEncrypter:
    def __init__(self):
        self.secret_key = b"1234567890123456"
    
    def password_encode(self, password):
        cipher = AES.new(self.secret_key, AES.MODE_CTR)
        ct_bytes = cipher.encrypt(password)
        nonce = b64encode(cipher.nonce).decode("utf-8")
        ct = b64encode(ct_bytes).decode("utf-8")
        result = json.dumps({'nonce': nonce, 'ciphertext': ct})
        print(result)
        return result

    def password_decode(self, password):
        cipher = AES.new(self.secret_key,AES.MODE_CTR) # never use ECB in strong systems obviously
        decoded = cipher.decrypt(password)
        print(decoded)
        return decoded
