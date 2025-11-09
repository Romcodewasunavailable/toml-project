"""
Script that fetches an example toml file from GitHub and parses it

Created on 2025.11.09
Contributors:
    Romain
"""

from display import print_data
import requests
import rtoml

URL = "https://raw.githubusercontent.com/toml-lang/toml-test/main/tests/valid/spec-example-1.toml"

REQUEST_FAILED_OUTPUT = "HTTP request failed. Status code: {}"


def main() -> None:
    response = requests.get(URL)
    if response.status_code == 200:
        print_data(rtoml.loads(response.text))
    else:
        print(REQUEST_FAILED_OUTPUT.format(response.status_code))


if __name__ == "__main__":
    main()
