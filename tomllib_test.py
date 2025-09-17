# -*- coding: utf-8 -*-
"""Just trying out how toml works

Created on 2025.09.17
@author: jakub.mnn
"""


import tomllib as tl


def main():
    with open("example0.toml", "rb") as file:
        toml = tl.load(file)
        print(toml)



if __name__ == "__main__":
    main()
