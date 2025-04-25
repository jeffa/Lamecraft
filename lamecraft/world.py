import random
from .crafting import INGREDIENTS

class World:
    def __init__(self, width, height, seed=None):
        self.width = width
        self.height = height
        if seed is None:
            seed = random.randint(0, 100000)
        self.seed = seed
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.generate()
        # Place ingredients on the world map
        self.place_ingredients()

    def generate(self):
        rng = random.Random(self.seed)
        for y in range(self.height):
            for x in range(self.width):
                v = rng.random()
                if v < 0.2:
                    biome = 'water'
                elif v < 0.3:
                    biome = 'sand'
                elif v < 0.7:
                    biome = 'grass'
                else:
                    biome = 'mountain'
                self.grid[y][x] = biome

    def get_tile(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.grid[y][x]

    def place_ingredients(self):
        """
        Randomly place ingredients throughout the world grid.
        """
        rng = random.Random(self.seed)
        # Map of (x, y) -> list of ingredient names
        self.items = {}
        # Randomly choose amount for each ingredient
        for ingredient in INGREDIENTS:
            count = rng.randint(0, 5)
            for _ in range(count):
                spawn_x = rng.randrange(self.width)
                spawn_y = rng.randrange(self.height)
                self.items.setdefault((spawn_x, spawn_y), []).append(ingredient)
