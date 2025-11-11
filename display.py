"""Code for displaying formatted data in the console.

Moved into a separate file.

Created on 2025.09.24
Contributors:
    Jakub
"""


indent_depth = 2
inline_list_max_length = 4


def format_dict(data: dict, leftpad: int=0) -> str:
    """Format the data contained in a dict to make it more human-readable."""
    result = ""
    for key in data.keys():
        value = data[key]

        padding = leftpad * ' '

        if type(value) is dict:
            result += f"\n{padding}[{key}]\n{format_dict(value, leftpad+indent_depth)}"

        elif type(value) is list and len(value) > inline_list_max_length:
            list_padding = (leftpad + indent_depth) * ' '

            bs = ',\n' # needed because python < 3.12 is stupid
                       # (backslashes aren't allowed in {} in f-strings)
            result += f"{padding}{key} = [\n{bs.join([list_padding + repr(element) for element in value])}\n{padding}]\n"
        
        # same as above, except for tuples instead of lists
        elif type(value) is tuple and len(value) > inline_list_max_length:
            list_padding = (leftpad + indent_depth) * ' '

            bs = ',\n' # needed because python < 3.12 is stupid
                       # (backslashes aren't allowed in {} in f-strings)
            result += f"{padding}{key} = (\n{bs.join([list_padding + repr(element) for element in value])}\n{padding})\n"

        else:
            result += f"{padding}{key} = {repr(value)}\n"

    return result


def print_data(data: dict) -> None:
    """Turn the data into a human-readable format and print to the console."""
    print(format_dict(data))
    
    
def _test() -> None:
    print("Beginning display library test...\n")
    print("====================================\n")
    
    data = {
        "foo": "bar",
        "Apples": ["Macintosh", "Gala", 260, "🍎", "Bad Apple"],
        "numbers": {
            "pie": 3.14159265,
            3: ["three", "trois", "drei", "trzy"],
            "Ϝ": 1,
            "bools": {
                True: False,
                "George Boole": None,
            },
            "position": (42, float("inf"), float("nan")),
        }
    }
    
    print_data(data)
    
    print("====================================\n")
    is_correct = input('Does the above data look properly formatted? (y/n): ').lower().startswith('y')
    
    assert is_correct
    print("Test passed !")


if __name__ == "__main__":
    _test()
