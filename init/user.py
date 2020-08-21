class UserClass():
    def __init__(self, list_of_choices):
        self.list_of_choices = list_of_choices
        pass

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