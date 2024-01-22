import argparse
from typing import Any


def create_parser() -> Any:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", nargs="*")
    parser.add_argument("-f", dest="file", nargs="*")

    return parser


if __name__ == '__main__':
    print(type(create_parser()))
