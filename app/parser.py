import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", nargs="*")
    parser.add_argument("-f", dest="file", nargs="*")

    return parser
