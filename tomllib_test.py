"""Example usage of tomllib.

Note: tomllib is only available on python 3.10+, while Thonny runs 3.9 by
default. Either update python version or run on spyder.

Created on 2025.09.17
Contributors:
    Jakub
"""


import tomllib as tl
from display import print_data


def main() -> None:
    """Execute the test program. Called when the script is executed."""
    with open("quark-common.toml", "rb") as file:
        toml = tl.load(file)
        print_data(toml)


if __name__ == "__main__":
    main()
