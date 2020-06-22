from init.database_creator import Creator
from automation.create_some_accounts import AccountCreatorAutomat
from sockets.server import ServerClass
from sockets.client import ClientClass


print("[Main.py] Starting Database Creator")
database_creator = Creator()
database_creator.create_db()
database_creator.create_client_table()

accounts_creator = AccountCreatorAutomat()
accounts_creator.create_multiple_accounts()
