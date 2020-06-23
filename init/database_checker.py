from init.database_creator import Creator
import pymysql as mysql

class Checker(Creator):
    def __init__(self):
        pass

    def check_if_database_exists(self):
        connection = self._connection()
        cursor = connection.cursor()
        try:
            cursor.execute("USE clients")
            number_of_databases = cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'clients'")
            print("[Database_checker.py] Database does exsists")
        except Exception:
            print("[Database_checker.py] Database does not exsists")

    def check_if_table_exists(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        number_of_tables = cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'clients' AND table_name = 'accounts'")
        print(number_of_tables)

    def check_if_accounts_in_table_exists(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        number_of_accounts = cursor.execute("SELECT COUNT(*) FROM accounts")
        print(number_of_accounts)