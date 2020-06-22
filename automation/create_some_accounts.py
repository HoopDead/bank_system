from init.database_creator import Creator
import mysql.connector
from mysql.connector import errorcode
import requests

class AccountCreatorAutomat(Creator):
    def __init__(self):
        pass

    def create_multiple_accounts(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        response = requests.get("https://randomuser.me/api")
        response.json()
        print(response.content)
        print("[Create_some_accounts.py] Creating accounts")