"""Toml implementation of a video game character save system

Created on 2025.11.05
Contributors:
    Romain
"""

from __future__ import annotations
from character import Character

INVALID_INPUT_OUTPUT = "Invalid input"


def main() -> None:
    while True:
        print("1) save a new character")
        print("2) load a stored character")
        try:
            choice = int(input("choice: "))
            assert choice in range(1, 3)
        except:
            print(INVALID_INPUT_OUTPUT)
        else:
            break

    match choice:
        case 1:
            character = Character.from_input()
        case 2:
            pass


if __name__ == "__main__":
    main()