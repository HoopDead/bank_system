from init.database_creator import CreatorClass
from auth.password_encrypt import AuthenticationPasswordEncrypterClass
from random import randint
import pymysql

class UserRegisterClass(CreatorClass, AuthenticationPasswordEncrypterClass):
    def __init__(self, first_name, last_name, password, country, city, street_name, home_number):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.country = country
        self.city = city
        self.street_name = street_name
        self.home_number = home_number


    def fetch_login_numbers(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        query = "SELECT login_number FROM accounts;"
        cursor.execute(query)
        result = cursor.fetchall()
        login_numbers = [int(item[0]) for item in result]
        return login_numbers

    def get_login_number(self):
        login_numbers = self.fetch_login_numbers()
        login_number = randint(11111111, 99999999)
        if login_number in login_numbers:
            return get_login_number()
        else:
            return login_number
            
    def register(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        auth_login = AuthenticationPasswordEncrypterClass()
        auth_login.set_secret_key()
        password_bytes = self.password.encode("utf-8")
        password_encode = auth_login.password_encode(password_bytes)
        login_number = self.get_login_number()
        account_number =  randint(11111111111111111111111111, 99999999999999999999999999)
        credit_card_number = randint(1111111111111111, 9999999999999999)
        cvv =  randint(100, 999)
        address = self.country + "," + self.city + "," + self.street_name + "," + self.home_number
        balance = 0
        statement = ("INSERT INTO accounts (name, surname, balance, address, account_number, creditcard, cvv, login_number, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (self.first_name, self.last_name, balance, address, account_number, credit_card_number, cvv, login_number, password_encode)
        try:
            print("[Register.py] Everything seems to be okay, your account is created. Your login number %s" % login_number)
            cursor.execute(statement, values)
            connection.commit()
        except pymysql.err.InternalError:
            print("Smth went wrong")