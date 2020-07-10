from base64 import b64encode, b64decode
from cryptography.fernet import Fernet
import json

class AuthenticationPasswordEncrypter:
    def __init__(self):
        self.secret_key = b""
        self.nonce = "+XyHurecq+U="
    
    def set_secret_key(self):
        with open('/mnt/d/Programs/Projekty/bank_system/auth/key.json') as key_json:
            key = json.load(key_json)
            key_variable = key['KEY']
            key_variable = key_variable.encode("utf-8")
            self.secret_key = key_variable

    def password_encode(self, password):
        return Fernet(self.secret_key).encrypt(password)
        
    def password_decode(self, password):
        try:
            return Fernet(self.secret_key).decrypt(password)
        except ValueError:
            print("Incorrect decryption")
