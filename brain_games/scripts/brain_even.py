#!usr/bin/env python3

from brain_games.engine import play
from brain_games.games import even

def main():
    """Brain-even game"""
    play(even)


if __name__ == '__main__':
    main()
