from init.database_creator import CreatorClass
from auth.password_encrypt import AuthenticationPasswordEncrypterClass

class UserLoginClass(CreatorClass, AuthenticationPasswordEncrypterClass):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        connection = self._connection()
        # self.set_secret_key()
        # print(self.password_encode("123"))
        print(self.username, self.password)