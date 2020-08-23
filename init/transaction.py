from init.database_creator import CreatorClass

class UserTransaction(CreatorClass):
    def __init__(self):
        pass

    def check_contact_list(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        query = "SELECT account_number, name, surname FROM accounts"
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception:
            print("[Transaction.py] There's a problem with connection, please check if everything is set and try again.")
            return None

    def make_transaction(self, user_balance, user_login_number, transaction_account_number, transaction_balance, ammount):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        user_balance_after_transaction = int(user_balance) - int(ammount)
        balance_after_transaction = int(transaction_balance) + int(ammount)
        query_user = "UPDATE accounts SET balance = %s WHERE login_number = %s"
        query_transaction = "UPDATE accounts SET balance = %s WHERE account_number = %s"    
        values_user = (user_balance_after_transaction, user_login_number)
        values_transaction = (transaction_account_number, transaction_balance)
        if user_balance > ammount:
            try:
                print("[Transaction.py] Passing your transaction for %s" % transaction_account_number)
                cursor.execute(query_user, values_user)
                connection.commit()   
                cursor.execute(query_transaction, values_transaction)
                connection.commit()
            except Exception:
                print("[Transaction.py] Error. Please check your data and try again.")
        else:
            print("[Transaction.py] You can't pass more money, than you have on your account!")
        # TODO - Function, that makes transaction working