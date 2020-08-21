from init.user import UserClass
from init.choices import LIST_OF_CHOICES
from auth.login import UserLoginClass
from auth.register import UserRegisterClass

def user_choice(choice, active_choices):
    if choice in active_choices:
        if choice == 1:
            print("[!] Do you want to log in?")
            user_login = UserLoginClass(input("Insert username: "), input("Insert password: "))
            password_encoded = user_login.get_password_from_db()
            if(password_encoded):
                user_login.login(password_encoded)
        if choice == 2:
            print("[!] Do you want to sign up?")
            user_register = UserRegisterClass(input("Insert your first name: "), input("Insert your last name: "), input("Insert your password: "), input("Insert your home country: "), input("Insert your city: "), input("Insert your street name: "), input("Insert your home number: "))
            user_register.register()
    else:
        print("[!] Please, provide a correct choice.")
        
if __name__ == "__main__":
    user = UserClass(LIST_OF_CHOICES)
    user_is_on = True
    user.introduction()
    user.display_choices()
    user.check_active_choices()
    while user_is_on:
        try:
            user_input = int(input("[?] Type your choice: "))
        except Exception:
            print("[!] You can't use text, just numbers.")
            user_input = 100
        if (user_input == -1):
            print("[!] Exit.")
            break
        user_choice(user_input, user.check_active_choices())