import json
import os
from menu import Menu
from world import World


def main():
    worlds = []

    menu = Menu()
    command = ""

    menu.print_phrase("hello")
    menu.help()

    # Read existing world data using json
    def read_world_data(worlds_list):
        dir = 'data/worlds/'
        world_data = []

        '''
        Loop through every .json file in worlds directory and read each one,
        adding dictionaries to world_data
        '''
        for filename in os.listdir(dir):
            file = open(os.path.join(dir, filename), 'r')
            jstr = file.read()
            jdict = json.loads(jstr)
            world_data.append(jdict)

        # Adding read parameters to world list
        for dictionary in world_data:
            worlds_list.append(World(dictionary['name'], dictionary['version'], dictionary['seed']))

        return worlds_list

    read_world_data(worlds)

    running = True
    while running:

        # Get command input
        print()
        command = menu.get_input("basic")
        print()
        # Check if command is correct and process it.'
        if command != False:
            # Process command
            command = menu.process_command(command)
            # Add world
            if command == menu.commands["aw"]:
                # Adds world to global world list.
                worlds.append(menu.get_input("add world"))

                # World that had just been added will be at the end of the list
                worlds[-1].write_world_data()
            # List worlds
            elif command == menu.commands["lw"]:
                menu.list_worlds(worlds)
            elif command == menu.commands["rw"]:
                menu.list_worlds(worlds)
                command = menu.get_input("remove world")

                for i in range(len(worlds)):
                    if worlds[i].name == command:
                        worlds[i].remove()
                        worlds.pop(i)
                        break
                else:
                    print("Either world with such name does not exist or operation canceled.\nOperation aborted.")

            # Quit
            elif command == menu.commands['q']:
                running = False
                menu.print_phrase("goodbye")
                break
        else:
            menu.print_phrase("error")


main()
