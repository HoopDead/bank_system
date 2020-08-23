from init.user import UserClass
from init.choices import LIST_OF_CHOICES, LIST_OF_CHOICES_AUTH
from auth.login import UserLoginClass
from auth.register import UserRegisterClass
from init.balance import UserBalance
from init.transaction import UserTransaction

def user_choice(choice, active_choices, user):
    if choice in active_choices:
        if choice == 1:
            user_login = UserLoginClass(input("Insert username: "), input("Insert password: "))
            password_encoded = user_login.get_password_from_db()
            if(password_encoded):
                user_login.login(password_encoded)
                user.update_active_choices(LIST_OF_CHOICES_AUTH)
                user.update_username(user_login.get_username())
        if choice == 2:
            user_register = UserRegisterClass(input("Insert your first name: "), input("Insert your last name: "), input("Insert your password: "), input("Insert your home country: "), input("Insert your city: "), input("Insert your street name: "), input("Insert your home number: "))
            user_register.register()
        if choice == 3:
            print("[!] Transaction")
            user_transaction = UserTransaction()
            user_balance = UserBalance(user.get_username())
            account_number = input("Insert account number for transaction: ")
            user_transaction.make_transaction(user_balance.get_account_balance(), user.get_username(), account_number, user_balance.get_account_balance_by_account_number(account_number), input("Insert ammount of money: "))
        if choice == 4:
            user_transaction = UserTransaction()
            user_list = user_transaction.check_contact_list()
            for contact in user_list:
                if(contact[0] != user.get_account_number()): #Exclude your own account number from contact list
                    print("%s %s, Acount Number: %s" % (contact[1], contact[2], contact[0]))
        if choice == 5:
            user_balance = UserBalance(user.get_username())
            print("[!] Your account balance is: %s" % user_balance.get_account_balance())
            # user_check_balance = UserCheckBalance(user.get_username())
            # print("[!] Your account balance %s" % user_check_balance.get_account_balance())
        if choice == 6:
            user_balance = UserBalance(user.get_username())
            user_balance.add_account_balance(input("Insert an ammount you want to have on your account: "))
        if choice == 7:
            print("[!] Your account number is %s" % user.get_account_number())
        if choice == 8:
            print("[!] Do you want to log out?")
            user.update_active_choices(LIST_OF_CHOICES)
    else:
        print("[!] Please, provide a correct choice.")
        
if __name__ == "__main__":
    user = UserClass(LIST_OF_CHOICES)
    user_is_on = True
    user.introduction()
    user.check_active_choices()
    while user_is_on:
        try:
            print("============")
            user.display_choices()
            user_input = int(input("[?] Type your choice: "))
        except Exception:
            print("[!] You can't use text, just numbers.")
            user_input = 100
        if (user_input == -1):
            print("[!] Exit.")
            user_is_on = False
            break
        user_choice(user_input, user.check_active_choices(), user)