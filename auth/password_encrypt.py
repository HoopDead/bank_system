from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
import json

class AuthenticationPasswordEncrypter:
    def __init__(self):
        self.secret_key = b"1234567890123456"
        self.nonce = "+XyHurecq+U="
    
    def password_encode(self, password):
        cipher = AES.new(self.secret_key, AES.MODE_CTR)
        ct_bytes = cipher.encrypt(password)
        nonce = b64encode(cipher.nonce).decode("utf-8")
        ct = b64encode(ct_bytes).decode("utf-8")
        result = json.dumps({'nonce': nonce, 'ciphertext': ct})
        print(result)
        return result

    def password_decode(self, password):
        try:
            b64 = json.loads(password)
            nonce = b64decode(b64['nonce'])
            ct = b64decode(b64['ciphertext'])
            cipher = AES.new(self.secret_key, AES.MODE_CTR, nonce=nonce)
            pt = cipher.decrypt(ct)
            print("The message was: ", pt)
            return pt
        except ValueError:
            print("Incorrect decryption")
