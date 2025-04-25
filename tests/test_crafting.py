import unittest
from lamecraft.inventory import Inventory
from lamecraft.crafting import CraftingSystem

class TestCrafting(unittest.TestCase):
    def test_craft_plank(self):
        inv = Inventory()
        inv.add_item('wood', 1)
        cs = CraftingSystem()
        item, qty = cs.craft(inv, ('wood',))
        self.assertEqual(item, 'plank')
        self.assertEqual(qty, 4)
        self.assertTrue(inv.has_item('plank', 4))

    def test_craft_missing_ingredient(self):
        inv = Inventory()
        cs = CraftingSystem()
        with self.assertRaises(ValueError):
            cs.craft(inv, ('wood',))

    def test_invalid_recipe(self):
        inv = Inventory()
        cs = CraftingSystem()
        with self.assertRaises(ValueError):
            cs.craft(inv, ('stone',))
