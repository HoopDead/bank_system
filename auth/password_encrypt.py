from base64 import b64encode, b64decode
from cryptography.fernet import Fernet
import json

class AuthenticationPasswordEncrypter:
    def __init__(self):
        self.secret_key = b"aGFvh3W74GXdeFPKdw1PcJBgrGknaioGLKB2nWIzie4="
        self.nonce = "+XyHurecq+U="
    
    def password_encode(self, password):
        return Fernet(self.secret_key).encrypt(password)
        
    def password_decode(self, password):
        try:
            return Fernet(self.secret_key).decrypt(password)
        except ValueError:
            print("Incorrect decryption")
