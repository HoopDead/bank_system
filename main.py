from init.database_creator import Creator
from automation.create_some_accounts import AccountCreatorAutomat

print("OK")
database_creator = Creator()
database_creator.create_db()
database_creator.create_client_table()

accounts_creator = AccountCreatorAutomat()
