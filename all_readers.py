"""Example usage of several toml modules.

Created on 2025.11.11
Contributors:
    Jakub
    Romain
"""


from display import print_data
import tomllib
import rtoml
import tomli


filepath = "quark-common.toml"
data = {}


def main():
    with open(filepath, "rb") as file:
        data["tomli"] = tomli.load(file)
        
    with open(filepath, "rb") as file:        
        data["tomllib"] = tomllib.load(file)
    
    # rtoml uses text instead of bytes
    with open(filepath, "rt") as file:
        data["rtoml"] = rtoml.load(file)
    
    print_data(data["tomllib"])
    

if __name__ == "__main__":
    main()
