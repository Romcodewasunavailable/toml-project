"""Usage example for rtoml

Created on 2025.09.24
Contributors:
    Romain
"""

from display import print_data
import rtoml
from pathlib import Path


def main():
    with open("quark-common.toml", "r") as file:
        data = rtoml.load(file)
        print_data(data)


if __name__ == "__main__":
    main()
