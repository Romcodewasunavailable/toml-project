"""Usage example for rtoml

Created on 2025.09.24
Contributors:
    Romain
"""

from display import print_data
import rtoml
from pathlib import Path


def main():
    data = rtoml.load(Path("quark-common.toml"))
    print_data(data)


if __name__ == "__main__":
    main()
