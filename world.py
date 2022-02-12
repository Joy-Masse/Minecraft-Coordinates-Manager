import json

# World class
class World:
    def __init__(self, name, version, seed):
        self.name = name
        self.version = version
        self.coordinates = []
        self.seed = seed

    def rename(self, new_name):
        self.name = new_name

    def edit_version(self, new_version):
        self.version = new_version

    def add_coordinates(self, new_coordinates):
        self.coordinates.append(new_coordinates)

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
