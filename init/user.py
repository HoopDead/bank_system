from init.database_creator import CreatorClass

class UserClass(CreatorClass):
    def __init__(self, list_of_choices):
        self.list_of_choices = list_of_choices
        self.username = None

    def introduction(self):
        print("[Bank Simulation System] === HELLO ===")
        print("[Bank Simulation System] Choose an option to continue.")

    def display_choices(self):
        for (index, choice) in enumerate(self.list_of_choices):
            if choice["active"]:
                print("[%i] %s" % (choice["id"], choice["message"]))

    def check_active_choices(self):
        active_choices = [i["id"] for i in self.list_of_choices if i["active"]]
        return active_choices

    def update_active_choices(self, updated_list_of_choices):
        self.list_of_choices = updated_list_of_choices
        print("[User.py] Updated list of choices!")

    def get_account_number(self):
        connection = self._connection()
        cursor = connection.cursor()
        cursor.execute("USE clients")
        query = "SELECT account_number FROM accounts WHERE login_number = %s;"
        try:
            sql = cursor.execute(query, (self.username))
            result = cursor.fetchone()
            return result[0]
        except Exception:
            print("[Check_balance.py] Something went wrong, please report bug on my github: https://github.com/hoopdead/")

    def update_username(self, username):
        self.username = username

    def get_username(self):
        return self.username