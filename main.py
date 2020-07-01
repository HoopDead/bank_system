from init.database_creator import Creator
from init.database_checker import Checker
from automation.create_some_accounts import AccountCreatorAutomat
from sockets.server import ServerClass
from sockets.client import ClientClass
from auth.password_encrypt import AuthenticationPasswordEncrypter
import json


print("[Main.py] Starting Database Creator")
#=== CLASS INIT AREA
database_creator = Creator()
database_checker = Checker()
accounts_creator = AccountCreatorAutomat()
password_encrypter = AuthenticationPasswordEncrypter()

database_creator.create_db()
database_creator.create_client_table()

password_encrypter.password_encode(b"test")

if (database_checker.check_if_database_exists()):
    pass
else:
    database_creator.create_db()

if (database_checker.check_if_table_exists()):
    pass
else:
    database_creator.create_client_table()

if (database_checker.check_if_accounts_in_table_exists()):
    pass
else:
    accounts_creator.create_multiple_accounts()