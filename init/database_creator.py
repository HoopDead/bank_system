import pymysql

class Creator:
    def __init__(self):
        pass

    def _connection(self):
        mydb = pymysql.connect(
            host = "127.0.0.1",
            user = "root",
            password = "123456"
        )
        return mydb

    def create_db(self):
        connection = self._connection()
        cursor = connection.cursor()
        try:
            cursor.execute("CREATE DATABASE clients")
        except Exception:
            print("[Database_Creator.py] Error (CONTINUE): Database already exsits")
            pass

    def create_client_table(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        try:
            cursor.execute("CREATE TABLE accounts (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), balance VARCHAR(16), address VARCHAR(255), account_number VARCHAR(26), creditcard VARCHAR(16), cvv VARCHAR(3), login_number VARCHAR(8), password VARCHAR(255))")
        except Exception:
            print("[Database_Creator.py] Error (CONTINUE): Table already exsits")
            pass
