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
            return True
        except Exception:
            print("[Database_checker.py] Database does not exsists")
            return False

    def check_if_table_exists(self):
        connection = self._connection()
        cursor = connection.cursor()
        try:
            cursor.execute("USE clients")
            number_of_tables = cursor.execute("SHOW TABLES LIKE 'accounts'")
            print("[Database_checker.py] Table does exsists")
            print(number_of_tables)
            return True
        except Exception:
            print("[Database_checker.py] Table does not exists")
            return False

    def check_if_accounts_in_table_exists(self):
        connection = self._connection()
        cursor = connection.cursor()
        try:
            cursor.execute("USE clients")
            number_of_accounts = cursor.execute("SELECT EXISTS(SELECT 1 FROM accounts)")
            print("[Database_checker.py] Table is not empty")
            return True
        except Exception:
            print("[Database_checker.py] Table accounts is empty")
            return False