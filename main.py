#!/usr/bin/env python3
import sys
import argparse

from lamecraft.game import run_game

def main():
    parser = argparse.ArgumentParser(description='Run Lamecraft')
    parser.add_argument('--width', type=int, default=50, help='World width')
    parser.add_argument('--height', type=int, default=30, help='World height')
    args = parser.parse_args()
    run_game(args.width, args.height)

if __name__ == '__main__':
    main()
