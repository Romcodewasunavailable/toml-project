"""Test dataclass for toml parsing testing

Created on 2025.10.01
Contributors:
    Romain
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Vector2():
    """Dummy 2d Vector class with no functionality"""
    x: float
    y: float


@dataclass(frozen=True)
class Character():
    """Save data for a video game character"""
    name: str
    birth_year: int
    position: Vector2