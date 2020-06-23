#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        for _ in range(25):
            response = requests.get("https://randomuser.me/api")
            r = response.json()
            person = {
                "first_name": r["results"][0]['name']['first'], 
                "last_name": r["results"][0]['name']['last'], 
                "address": r["results"][0]["location"]["country"] + ", " + r["results"][0]["location"]["city"] + ", " + r["results"][0]["location"]["street"]["name"] + ", " + str(r["results"][0]["location"]["street"]["number"]), 
                "account_number": randint(11111111111111111111111111, 99999999999999999999999999), 
                "credit_card_number": randint(1111111111111111, 9999999999999999), 
                "cvv": randint(100, 999),
                "login_number": randint(11111111, 99999999), 
                "password": r["results"][0]["login"]["password"]
            }
            statement = ("INSERT INTO accounts (name, surname, address, account_number, creditcard, cvv, login_number, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            values = (person["first_name"], person["last_name"], person["address"], person["account_number"], person["credit_card_number"], person["cvv"], person["login_number"], person["password"])
            cursor.execute(statement, values)
            connection.commit()