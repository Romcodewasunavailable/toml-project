"""Just trying out how toml works

Created on 2025.09.17
Contributors:
    Jakub
"""


import tomllib as tl
from display import print_data


def main() -> None:
    """Executes the test program. Called when the script is executed."""
    with open("quark-common.toml", "rb") as file:
        toml = tl.load(file)
        print_data(toml)



if __name__ == "__main__":
    main()
