from init.database_creator import CreatorClass
import pymysql

class UserBalance(CreatorClass):
    def __init__(self, login_number):
        self.login_number = login_number

    def get_account_balance(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        query = "SELECT balance FROM accounts WHERE login_number = %s;"
        try:
            sql = cursor.execute(query, (self.login_number))
            result = cursor.fetchone()
            return result[0]
        except Exception:
            print("[Check_balance.py] Something went wrong, please report bug on my github: https://github.com/hoopdead/")

    def add_account_balance(self, ammount):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        statement = ("UPDATE accounts SET balance = %s WHERE login_number = %s")
        values = (ammount, self.login_number)
        try:
            print("[Balance.py] Updating your account with balance %s" % ammount)
            cursor.execute(statement, values)
            connection.commit()
        except pymysql.err.InternalError:
            print("[Balance.py] Something went wrong - please check your data and try again.")