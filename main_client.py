from init.user import UserClass
from init.choices import LIST_OF_CHOICES
from auth.login import UserLoginClass

def user_choice(choice, active_choices):
    if choice in active_choices:
        if choice == 1:
            print("[!] Do you want to log in?")
            user_login = UserLoginClass(input("Wprowadź nazwę użytkownika: "), input("Wprowadź hasło: "))
            user_login.login()
        if choice == 2:
            print("[!] Do you want to sign up?")
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