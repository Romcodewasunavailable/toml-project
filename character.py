"""Example dataclass for data parsing testing

Created on 2025.10.01
Contributors:
    Romain
"""

from __future__ import annotations
from dacite import from_dict
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Vector2():
    """Dummy 2d Vector class with no functionality"""
    x: float
    y: float


@dataclass(frozen=True)
class Character():
    """Save data for a video game character"""
    name: str
    age: int
    position: Vector2
    inventory: dict[str, int]

    @classmethod
    def test_character(cls) -> Character:
        """Sample character with arbitrary attributes for testing"""
        return cls(
            "Bob",
            21,
            Vector2(
                42.0,
                -3.14,
            ),
            {
                "Apple": 3,
                "Sword": 1,
                "Healing Potion": 2,
                "Jakub": 1,
            },
        )

    @classmethod
    def from_input(cls) -> Character:
        """"""
        name = input("name: ")
        age = int(input("age: "))
        position = Vector2(
            float(input("x position: ")),
            float(input("y position: ")),
        )
        inventory = {}
        print("inventory (type done to finish):")
        while True:
            item = input("add item: ")
            if item == "done":
                break
            elif item in inventory:
                inventory[item] += 1
            else:
                inventory[item] = 1

        return cls(
            name,
            age,
            position,
            inventory,
        )

    @classmethod
    def from_dict(cls, data: dict) -> Character:
        """"""
        return from_dict(cls, data)

    def to_dict(self) -> dict:
        """"""
        return asdict(self)


def test() -> None:
    character = Character.test_character()
    character_dict = character.to_dict()
    print(character_dict)
    character_rebuilt = Character.from_dict(character_dict)
    print(character_rebuilt)
    assert character_rebuilt == character
    print("Tests passed !")


if __name__ == "__main__":
    test()
