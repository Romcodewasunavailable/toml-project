"""Toml implementation of a video game character save system.

Created on 2025.11.05
Contributors:
    Romain
    Jakub
"""

from __future__ import annotations
from character import Character
import rtoml

TOML_EXTENSION = ".toml"

ACTIONS_OUTPUT = """\n1) Save a new character
2) Load a stored character
3) Quit"""
CHARACTER_SAVED_OUTPUT = "\nCharacter saved"
FILE_NOT_FOUND_OUTPUT = "\nFile not found"
INVALID_INPUT_OUTPUT = "\nInvalid input"

CHOICE_PROMPT = "\nChoice: "
FILE_NAME_PROMPT = "\nFile name: "


def input_toml_file_name() -> str:
    """Ask the user for a .toml file."""
    file_name = input(FILE_NAME_PROMPT)
    if not file_name.endswith(TOML_EXTENSION):
        file_name += TOML_EXTENSION

    return file_name


def main() -> None:
    """Execute the test program. Called when the script is executed."""
    while True:
        print(ACTIONS_OUTPUT)
        choice = input(CHOICE_PROMPT)
        match choice:
            case "1":
                with open(input_toml_file_name(), "w") as file:
                    rtoml.dump(Character.from_input().to_dict(), file)
                print(CHARACTER_SAVED_OUTPUT)

            case "2":
                try:
                    with open(input_toml_file_name(), "r") as file:
                        print(Character.from_dict(rtoml.load(file)))
                except FileNotFoundError:
                    print(FILE_NOT_FOUND_OUTPUT)

            case "3":
                quit()

            case _:
                print(INVALID_INPUT_OUTPUT)


if __name__ == "__main__":
    main()
