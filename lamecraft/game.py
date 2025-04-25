from .world import World
from .player import Player
from .ui import GameUI

def run_game(width=50, height=30):
    world = World(width, height)
    player = Player(width // 2, height // 2)
    ui = GameUI(world, player)
    ui.run()
