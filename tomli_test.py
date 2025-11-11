"""Usage example for tomli

Created on 2025.09.24
Contributors:
    Romain
    Jakub
"""

from display import print_data
import tomli
#import tomli_w


def main() -> None:
    """Execute the test program. Called when the script is executed."""
    with open("quark-common.toml", "rb") as file:
        data = tomli.load(file)
        print_data(data)


if __name__ == "__main__":
    main()
