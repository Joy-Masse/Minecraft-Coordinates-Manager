import json
from menu import Menu
from world import World

def main():
    worlds = []

    menu = Menu()
    command = ""

    menu.print_phrase("hello")
    menu.help()

    running = True
    while running:

        # Get command input
        print()
        command = menu.get_input("basic")
        print()
        # Check if command is correct and process it.
        if command != False:
            # Process command
            command = menu.process_command(command)

            # Add world
            if command == menu.commands["aw"]:
                worlds.append(menu.get_input("add world"))
                print(worlds[0].name, worlds[0].seed, worlds[0].version)
            elif command == menu.commands["lw"]:
                menu.list_worlds(worlds)
            # Quit
            elif command == menu.commands['q']:
                running = False
                menu.print_phrase("goodbye")
                break
        else:
            menu.print_phrase("error")

main()
