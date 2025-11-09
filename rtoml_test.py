"""Usage example for rtoml

Created on 2025.09.24
Contributors:
    Romain
    Jakub
"""

from display import print_data
import rtoml
from pathlib import Path


def main() -> None:
    """Executes the test program. Called when the script is executed."""
    with open("quark-common.toml", "r") as file:
        data = rtoml.load(file)
        print_data(data)


if __name__ == "__main__":
    main()
