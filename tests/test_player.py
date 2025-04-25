import unittest
from lamecraft.player import Player
from lamecraft.world import World

class TestPlayer(unittest.TestCase):
    def test_move_within_bounds(self):
        world = World(5, 5, seed=0)
        player = Player(2, 2)
        moved = player.move(1, 0, world)
        self.assertTrue(moved)
        self.assertEqual((player.x, player.y), (3, 2))

    def test_move_out_of_bounds(self):
        world = World(5, 5, seed=0)
        player = Player(0, 0)
        moved = player.move(-1, 0, world)
        self.assertFalse(moved)
        self.assertEqual((player.x, player.y), (0, 0))
