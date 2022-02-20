import json
from os import remove as rm

# World class


class World:
    # Constructor
    def __init__(self, name, version, seed):
        self.name = name
        self.version = version
        self.coordinates = []
        self.seed = seed

    # Change world name
    def rename(self, new_name):
        self.name = new_name

    # Edit version
    def edit_version(self, new_version):
        self.version = new_version

    # Add new coordinates
    def add_coordinates(self, new_coordinates):
        self.coordinates.append(new_coordinates)

    # Edit seed
    def edit_seed(self, new_seed):
        self.seed = new_seed

    # JSON
    def write_world_data(self):
        world_file = open("data/worlds/" + self.name + ".json", "w")

        world = {"name": self.name,
                 "version": self.version,
                 "seed": self.seed
                 }

        string = json.dumps(world)
        world_file.write(string)
        world_file.close()

    # Remove world
    def remove(self):
        rm(f"data/worlds/{self.name}.json")
