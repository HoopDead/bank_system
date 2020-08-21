from init.user import UserClass
from init.choices import LIST_OF_CHOICES, LIST_OF_CHOICES_AUTH
from auth.login import UserLoginClass
from auth.register import UserRegisterClass

def user_choice(choice, active_choices, user):
    if choice in active_choices:
        if choice == 1:
            print("[!] Do you want to log in?")
            user_login = UserLoginClass(input("Insert username: "), input("Insert password: "))
            password_encoded = user_login.get_password_from_db()
            if(password_encoded):
                user_login.login(password_encoded)
                user.update_active_choices(LIST_OF_CHOICES_AUTH)
        if choice == 2:
            print("[!] Do you want to sign up?")
            user_register = UserRegisterClass(input("Insert your first name: "), input("Insert your last name: "), input("Insert your password: "), input("Insert your home country: "), input("Insert your city: "), input("Insert your street name: "), input("Insert your home number: "))
            user_register.register()
        if choice == 4:
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