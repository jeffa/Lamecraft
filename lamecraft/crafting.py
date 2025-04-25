from .inventory import Inventory

# List of raw ingredients that can be placed in the world
INGREDIENTS = [
    'wood', 'cobblestone', 'iron_ore', 'coal', 'sand', 'leather', 'string',
    'feather', 'flint', 'cactus', 'sugar_cane', 'wheat', 'potato', 'carrot',
    'bone', 'ink_sac', 'glass', 'clay', 'wool', 'egg'
]

# List of craftable items
ITEMS = [
    'plank', 'stick', 'torch', 'stone_pickaxe', 'iron_ingot', 'iron_pickaxe',
    'bread', 'arrow', 'bow', 'cake'
]

class CraftingSystem:
    def __init__(self, recipes=None):
        # Initialize with default recipes if none provided
        if recipes is None:
            # recipes: tuple of input item names -> (output item, quantity)
            self.recipes = {
                # Basic wood processing
                ('wood',): ('plank', 4),
                ('plank',): ('stick', 4),

                # Torches from wood and coal
                ('wood', 'coal'): ('torch', 4),

                # Stone pickaxe: 3 cobblestone + 2 sticks
                ('cobblestone', 'cobblestone', 'cobblestone', 'stick', 'stick'): ('stone_pickaxe', 1),

                # Smelt iron ore into iron ingot
                ('iron_ore', 'coal'): ('iron_ingot', 1),

                # Iron pickaxe: 3 iron ingots + 2 sticks
                ('iron_ingot', 'iron_ingot', 'iron_ingot', 'stick', 'stick'): ('iron_pickaxe', 1),

                # Bread from wheat
                ('wheat', 'wheat', 'wheat'): ('bread', 1),

                # Arrows: 1 feather + 1 stick -> 4 arrows
                ('feather', 'stick'): ('arrow', 4),

                # Bow: 3 string + 2 sticks
                ('string', 'string', 'string', 'stick', 'stick'): ('bow', 1),

                # Cake: 3 milk buckets (simulated as 'egg'), 2 sugar, 3 wheat
                ('egg', 'sugar_cane', 'sugar_cane', 'sugar_cane', 'wheat', 'wheat', 'wheat'): ('cake', 1),
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
