from init.database_creator import Creator
from init.database_checker import Checker
from automation.create_some_accounts import AccountCreatorAutomat
from sockets.server import ServerClass
from sockets.client import ClientClass


print("[Main.py] Starting Database Creator")
# database_creator = Creator()
# database_creator.create_db()
# database_creator.create_client_table()

database_checker = Checker()
database_checker.check_if_database_exists()
database_checker.check_if_accounts_in_table_exists()
database_checker.check_if_table_exists()


# accounts_creator = AccountCreatorAutomat()
# accounts_creator.create_multiple_accounts()
