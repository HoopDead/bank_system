from init.database_creator import Creator
import pymysql as mysql
import requests
from random import randint

class AccountCreatorAutomat(Creator):
    def __init__(self):
        pass

    def create_multiple_accounts(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        response = requests.get("https://randomuser.me/api")
        r = response.json()
        first_name = r["results"][0]['name']['first']
        last_name = r["results"][0]['name']['last']
        address = (r["results"][0]["location"]["country"] + ", " + r["results"][0]["location"]["city"] + ", " + r["results"][0]["location"]["street"]["name"] + ", " + str(r["results"][0]["location"]["street"]["number"]))
        account_number = randint(11111111111111111111111111, 99999999999999999999999999)
        credit_card_number = randint(1111111111111111, 9999999999999999)
        cvv = randint(100, 999)
        login_number = randint(11111111, 99999999)
        password = r["results"][0]["login"]["password"]
        print("[Create_some_accounts.py] Creating new accounts \n First name: %s\n Last name: %s\n Address: %s\n Account Number: %i \n Credit Card Number: %i \n CVV: %i \n Login number: %i \n Password: %s \n" % (first_name, last_name, address, account_number, credit_card_number, cvv, login_number, password))
