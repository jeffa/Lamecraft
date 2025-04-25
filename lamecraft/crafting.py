from .inventory import Inventory

class CraftingSystem:
    def __init__(self, recipes=None):
        if recipes is None:
            self.recipes = {
                ('wood',): ('plank', 4),
                ('plank',): ('stick', 4)
            }
        else:
            self.recipes = recipes

    def craft(self, inventory: Inventory, recipe_key):
        if recipe_key not in self.recipes:
            raise ValueError('Recipe does not exist')
        input_items = recipe_key
        for item in input_items:
            if not inventory.has_item(item):
                raise ValueError(f'Missing ingredient: {item}')
        out_item, out_qty = self.recipes[recipe_key]
        for item in input_items:
            inventory.remove_item(item)
        inventory.add_item(out_item, out_qty)
        return out_item, out_qty
