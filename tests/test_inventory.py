import unittest
from lamecraft.inventory import Inventory

class TestInventory(unittest.TestCase):
    def test_add_and_remove(self):
        inv = Inventory()
        inv.add_item('wood', 3)
        self.assertTrue(inv.has_item('wood', 3))
        inv.remove_item('wood', 2)
        self.assertTrue(inv.has_item('wood', 1))
        inv.remove_item('wood', 1)
        self.assertFalse(inv.has_item('wood'))
        with self.assertRaises(ValueError):
            inv.remove_item('wood')

    def test_get_items(self):
        inv = Inventory()
        inv.add_item('stone', 5)
        items = inv.get_items()
        self.assertEqual(items, {'stone': 5})
