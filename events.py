from .names import LocationNames, ItemNames

def create_events(world, player):
    world.get_location(LocationNames.victory , player).place_locked_item(world.create_item(ItemNames.victory, player))
