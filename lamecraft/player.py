from .inventory import Inventory

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.inventory = Inventory()

    def move(self, dx, dy, world):
        new_x = self.x + dx
        new_y = self.y + dy
        if world.get_tile(new_x, new_y) is not None:
            self.x = new_x
            self.y = new_y
            return True
        return False
