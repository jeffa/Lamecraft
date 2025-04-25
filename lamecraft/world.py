import random

class World:
    def __init__(self, width, height, seed=None):
        self.width = width
        self.height = height
        if seed is None:
            seed = random.randint(0, 100000)
        self.seed = seed
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.generate()

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
