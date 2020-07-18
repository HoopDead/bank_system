from init.database_creator import Creator
import pymysql

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
        cursor.execute("USE clients")
        try:
            number_of_tables = cursor.execute("show tables like 'accounts';")
            print("[Database_checker.py] Table does exsists")
            return True
        except Exception:
            print("[Database_checker.py] Table does not exists")
            return False

    def check_if_accounts_in_table_exists(self):
        connection = self._connection()
        cursor = connection.cursor()
        try:
            cursor.execute("USE clients")
            number_of_accounts = cursor.execute("SELECT * FROM accounts;")
            print("[Database_checker.py] Number of accounts in table %s" % number_of_accounts)
            if (number_of_accounts < 1):
                print("[Database_checker.py] Table is empty - adding some test accounts")
                return False
            else:
                print("[Database_checker.py] Table is not empty")
                return True
        except Exception:
            print("[Database_checker.py] Mysql ERROR")
            return False