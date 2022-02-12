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
        # Check if command is correct and process it.
        if command != False:
            # Process command
            command = menu.process_command(command)

            # Add world
            if command == menu.commands["aw"]:
                worlds.append(menu.get_input("add world"))
                # World that has just been added will be at the end of the list
                worlds[-1].write_world_data()
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
