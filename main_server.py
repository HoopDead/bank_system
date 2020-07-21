from init.database_creator import CreatorClass
from init.database_checker import CheckerClass
from automation.create_some_accounts import AccountCreatorAutomatClass
from sockets.server import ServerClass
from sockets.server_info import SERVER, ADDR
from auth.password_encrypt import AuthenticationPasswordEncrypterClass
import json


print("[Main_Server.py] Starting Database Creator")
#=== CLASS INIT AREA
database_creator = CreatorClass()
database_checker = CheckerClass()
accounts_creator = AccountCreatorAutomatClass()
password_encrypter = AuthenticationPasswordEncrypterClass()
server_class = ServerClass(SERVER, ADDR)

database_creator.create_db()
database_creator.create_client_table()

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

server_class.start()