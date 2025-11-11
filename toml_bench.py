"""Script for comparing execution time of different toml modules.

Created on 2025.10.01
Contributors:
    Romain
    Jakub
"""


from benchtime import benchtime, print_bench
import rtoml
import tomli
try:
    import tomllib
except ModuleNotFoundError:
    print("Tomllib module not found, update thonny python version to 3.10+ or run on spyder to benchmark it as well\n")
    tomllib = None


TOML_FILE_PATH = "quark-common.toml"
ITERATIONS = 100


def main() -> None:
    """Execute the test program. Called when the script is executed."""
    for i in range(ITERATIONS):
        load_rtoml(TOML_FILE_PATH)
        load_tomli(TOML_FILE_PATH)
        if tomllib:
            load_tomllib(TOML_FILE_PATH)
    print(f"Average reading time for {TOML_FILE_PATH} over {ITERATIONS} iterations:")
    print_bench()


@benchtime("rtoml")
def load_rtoml(file_path: str) -> dict:
    """Test the performance of RTOML."""
    with open(file_path, "r") as file:
        return rtoml.load(file)


@benchtime("tomli")
def load_tomli(file_path: str) -> dict:
    """Test the performance of TOMLI."""
    with open(file_path, "rb") as file:
        return tomli.load(file)


@benchtime("tomllib")
def load_tomllib(file_path: str) -> dict:
    """Test the performance of TOMLLIB."""
    with open(file_path, "rb") as file:
        return tomllib.load(file)


if __name__ == "__main__":
    main()
