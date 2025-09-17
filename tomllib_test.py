# -*- coding: utf-8 -*-
"""Just trying out how toml works

Created on 2025.09.17
@author: jakub.mnn
"""


import tomllib as tl


indent_depth = 2
inline_list_max_length = 4


def main():
    with open("quark-common.toml", "rb") as file:
        toml = tl.load(file)
        print_data(toml)


def format_dict(data: dict, leftpad: int=0) -> str:

    result = ""
    for key in data.keys():
        value = data[key]

        padding = leftpad * ' '

        if type(value) is dict:
            result += f"\n{padding}[{key}]\n{format_dict(value, leftpad+indent_depth)}"

        elif type(value) is list and len(value) > inline_list_max_length:
            list_padding = (leftpad + indent_depth) * ' '
            result += f"{padding}{key} = [\n{',\n'.join([list_padding + repr(element) for element in value])}\n{padding}]\n"

        else:
            result += f"{padding}{key} = {value}\n"

    return result


def print_data(data: dict) -> None:
    """Turn the data into a human-readable format and print to the console."""
    print(format_dict(data))


if __name__ == "__main__":
    main()
