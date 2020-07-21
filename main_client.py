from init.user import UserClass
from init.choices import LIST_OF_CHOICES


if __name__ == "__main__":
    user = UserClass(LIST_OF_CHOICES)
    user_is_on = True
    user.introduction()
    user.display_choices()
    while user_is_on:
        try:
            a = int(input())
        except Exception:
            print("[!] You can't use text, just numbers.")
        if (a == -1):
            print("[!] Exit.")
            break
        for i in LIST_OF_CHOICES:
            if i["id"] == a:
                print("OK")
            else:
                print("[!] You must insert a correct choice!")