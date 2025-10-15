"""Test dataclass for toml parsing testing

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
class Item():
    """Inventory filling material"""
    name: str


@dataclass(frozen=True)
class Character():
    """Save data for a video game character"""
    name: str
    age: int
    position: Vector2
    inventory: dict[Item, int]

    @classmethod
    def test_character(cls) -> Character:
        """Sample character with arbitrary attributes for testing"""
        return cls(
            "Bob",
            21,
            Vector2(42.0, -3.14),
            {
                Item("Apple"): 3,
                Item("Sword"): 1,
                Item("Healing Potion"): 2,
                Item("Jakub ;)"): 1,
            }
        )
    
    @classmethod
    def from_dict(cls, data: dict) -> Character:
        """"""
        return from_dict(cls, data)

    def to_dict(self) -> dict:
        """"""
        return asdict(self)
        
