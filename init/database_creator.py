import mysql.connector
from mysql.connector import errorcode

class Creator:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def __connection(self):
        mydb = mysql.connector.connect(
            host = self.host,
            user = self.username,
            password = self.password
        )
        return mydb

    def create_db(self):
        con = self.__connection()
        cursor = con.cursor()
        cursor.execute("CREATE DATABASE clients")
        print("OK!")