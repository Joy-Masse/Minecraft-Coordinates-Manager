from world import World

# Main menu
class Menu:
    def __init__(self):
        self.phrases = {
        "hello": "Welcome to Minecraft Coordinates Manager!\n",
        "error": "ERROR: No such command.\n",
        "goodbye": "Hope you enjoyed using Minecraft Coordinates Manager!\n"
        }

        self.options = ["This Menu", "Add World", "List Worlds",
                        "Remove World", "Quit"]
        self.commands = {"help": "Help", "lw": "List Worlds",
                        "aw": "Add World", "rw": "Remove World", "q": "Quit"}

    # Prints selected phrase if it is in list of phrases
    def print_phrase(self, phrase):
        if phrase in self.phrases:
            print(self.phrases[phrase])
        else:
            print("ERROR: Invalid phrase. Please contact the developer.\n")

    # BEWARE! HARDCODED!!!
    def help(self):
        help_phrase = ""
        help_commands = ["help", "aw", "lw", "rw", "q"]

        print("Help menu:")
        for i in range(len(self.options)):
            help_phrase += help_commands[i] + " - " + self.options[i] + "\n"

        print(help_phrase)

    # Gets input from user to interact with them. Returns False if user is wrong
    # Modes:
    # "basic" - basic mode of operation (Help, Add Worlds, Remove Worlds, etc.)
    # "add world" - Gets input to add world (name, seed...)
    def get_input(self, mode):
        modes = ("basic", "add world")

        # Check to see if mode is correct
        if mode in modes:
            # "basic"
            if mode == "basic":
                input_var = input("Command: ")

                if input_var in self.commands:
                    return input_var
                else:
                    return False
            # "add world"
            elif mode == "add world":
                print("Adding world...\n")

                name = input("World Name: ")
                version = input("Game Version: ")
                seed = input("Seed: ")

                return World(name, version, seed)
        else:
            print("ERROR: Invalid 'get_input' mode. Contact the developer.")

    # Lists wolrds
    def list_worlds(self, worlds_list):
        # Check to see if worlds exists
        if len(worlds_list) > 0:
            # Print worlds
            for i in range(len(worlds_list)):
                # Name
                print(worlds_list[i].name + ":")
                # Everything else
                print("\tVersion: " + worlds_list[i].version + "\n\tSeed: " + worlds_list[i].seed + "\n")
        # In case worlds do not exist
        else:
            print("No Worlds Found\n")

    # Process command entered by the user.
    def process_command(self, input_var):
        result = self.commands[input_var]

        # VERY UGLY
        if result == self.commands["help"]:
            self.help()
        # Add world
        elif result == self.commands["aw"]:
            return self.commands["aw"]
        elif result == self.commands["lw"]:
            return self.commands["lw"]
        elif result == self.commands["rw"]:
            print("NOT YET IMPLEMENTED")
        elif result == self.commands["q"]:
            return self.commands["q"]
