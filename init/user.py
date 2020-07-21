class UserClass:
    def __init__(self, list_of_choices):
        self.list_of_choices = list_of_choices
        pass

    def introduction(self):
        print("[Bank Simulation System] === HELLO ===")
        print("[Bank Simulation System] Choose an option to continue.")

    def display_choices(self):
        for (index, choice) in enumerate(self.list_of_choices):
            if choice["active"]:
                print("[%i] %s" % (index, choice["message"]))