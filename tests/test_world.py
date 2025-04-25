import unittest
from lamecraft.world import World

class TestWorld(unittest.TestCase):
    def test_generate_consistency(self):
        w1 = World(10, 10, seed=42)
        w2 = World(10, 10, seed=42)
        self.assertEqual(w1.grid, w2.grid)

    def test_get_tile_out_of_bounds(self):
        w = World(5, 5)
        self.assertIsNone(w.get_tile(-1, 0))
        self.assertIsNone(w.get_tile(0, 5))
        self.assertIsNone(w.get_tile(5, 0))
        self.assertIsNone(w.get_tile(0, -1))
