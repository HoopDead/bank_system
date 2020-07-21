#!/usr/bin/python
# -*- coding: utf-8 -*-

from init.database_creator import CreatorClass
from auth.password_encrypt import AuthenticationPasswordEncrypterClass
import pymysql
import requests
from random import randint

class AccountCreatorAutomatClass(CreatorClass):
    def __init__(self):
        pass

    def create_multiple_accounts(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        for _ in range(8):
            response = requests.get("https://randomuser.me/api")
            r = response.json()
            person = {
                "first_name": r["results"][0]['name']['first'].encode("utf-8"), 
                "last_name": r["results"][0]['name']['last'].encode("utf-8"),
                "balance": randint(100, 10000),
                "address": r["results"][0]["location"]["country"] + ", " + r["results"][0]["location"]["city"] + ", " + r["results"][0]["location"]["street"]["name"] + ", " + str(r["results"][0]["location"]["street"]["number"]), 
                "account_number": randint(11111111111111111111111111, 99999999999999999999999999), 
                "credit_card_number": randint(1111111111111111, 9999999999999999), 
                "cvv": randint(100, 999),
                "login_number": randint(11111111, 99999999), 
                "password": r["results"][0]["login"]["password"]
            }
            password_encrypter = AuthenticationPasswordEncrypter()
            password_encrypter.set_secret_key()
            password = password_encrypter.password_encode(person["password"].encode("utf-8"))
            statement = ("INSERT INTO accounts (name, surname, balance, address, account_number, creditcard, cvv, login_number, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            values = (person["first_name"], person["last_name"], person["balance"], person["address"], person["account_number"], person["credit_card_number"], person["cvv"], person["login_number"], password)
            try:
                cursor.execute(statement, values)
            except pymysql.err.InternalError:
                print("[Create_some_accounts.py] There's some non utf-8 enoding in person object. Passing error and not adding this value to database.")
            connection.commit()