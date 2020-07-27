from init.database_creator import CreatorClass
from auth.password_encrypt import AuthenticationPasswordEncrypterClass

class UserLoginClass(CreatorClass, AuthenticationPasswordEncrypterClass):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_password_from_db(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        query = "SELECT password FROM accounts WHERE login_number = %s;"
        try:
            login = cursor.execute(query, (self.username))
            result = cursor.fetchone()
            return result[0]
        except Exception:
            print("[Login.py] Username or Password is incorrect!")

    def login(self, password):
        connection = self._connection()
        auth_login = AuthenticationPasswordEncrypterClass()
        auth_login.set_secret_key()
        password_bytes = b""
        password_bytes = password.encode("utf-8")
        password_encode = auth_login.password_decode(password_bytes)
        password_decode = password_encode.decode("utf-8")
        if(password_decode == self.password):
            print("[Login.py] Everything is okay, redirect to logged in user.")
        else:
            print("[Login.py] Username or Password is incorrect!")

