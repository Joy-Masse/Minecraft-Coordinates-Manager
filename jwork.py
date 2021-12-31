import json
from world import World

def write_world_data(world):
    world_file = open("data/worlds" + world.name + ".json", "w")

    world = {"name": world.name,
            "version": world.version,
            "seed": world.seed
            }

    string = json.dumps(world)
    world_file.write(string)
    world_file.close()

world = World("nass")
world.edit_seed(10000)
write_world_data(world)
