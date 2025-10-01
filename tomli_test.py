"""Usage example for tomli/tomli-w

Created on 2025.09.24
Contributors:
    Romain
"""

from display import print_data
import tomli
import tomli_w


def main():
    with open("quark-common.toml", "rb") as file:
        data = tomli.load(file)
        print_data(data)


if __name__ == "__main__":
    main()
