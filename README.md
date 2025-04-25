# Lamecraft

A 2D sandbox survival game (Python + PyQt5) inspired by Minecraft.

## Features

- Procedurally generated 2D tile-based world with biomes (water, sand, grass, mountain) using a seeded random generator.
- Resource gathering and basic block interaction.
- Simple crafting system.
- Grid-based building mechanics.

## Installation

1. Clone the repository:
   ```
   git clone <repo_url>
   cd <repo_folder>
   ```
2. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the game with default settings:
```
python main.py
```

Specify world size:
```
python main.py --width 100 --height 50
```

## Running Tests

Use unittest:
```
python -m unittest discover
```

## Project Structure

```
.
├── lamecraft
│   ├── __init__.py
│   ├── world.py
│   ├── player.py
│   ├── inventory.py
│   ├── crafting.py
│   ├── ui.py
│   └── game.py
├── tests
│   ├── test_world.py
│   ├── test_inventory.py
│   ├── test_crafting.py
│   └── test_player.py
├── main.py
├── requirements.txt
└── README.md
```
