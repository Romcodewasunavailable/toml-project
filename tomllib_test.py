# -*- coding: utf-8 -*-
"""Just trying out how toml works

Created on 2025.09.17
@author: jakub.mnn
"""


import tomllib as tl


def main():
    with open("example0.toml", "rb") as file:
        toml = tl.load(file)
        print_data(toml)


def format_dict(data: dict, leftpad: int=0) -> str:

    result = ""
    for key in data.keys():
        value = data[key]

        if type(value) is dict:
            result += f"\n{leftpad*' '}[{key}]\n{format_dict(value, leftpad+2)}"

        else:
            result += f"{leftpad*' '}{key} = {value}\n"

    return result




def print_data(data: dict) -> None:
    """Turn the data into a human-readable format and print to the console."""
    print(format_dict(data))


if __name__ == "__main__":
    main()
