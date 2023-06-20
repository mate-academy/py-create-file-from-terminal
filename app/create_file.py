from argparse import ArgumentParser
from datetime import datetime
from os import path, makedirs


def main(arguments: dict) -> None:
    dir_path = None
    if arguments["d"] and not path.exists(
        dir_path := path.join(*arguments["d"])
    ):
        makedirs(path.join(*arguments["d"]))
    if arguments["f"]:
        file_path = path.join(f"{dir_path or ''}", arguments["f"])
        __add_file_content(file_path)


def __add_file_content(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(f"{datetime.now().strftime('%Y.%m.%d %H:%M:%S')}\n")
        while (line := input("Enter content line: ")) != "stop":
            file.write(f"{line}\n")


if __name__ == '__main__':
    args_parser = ArgumentParser()
    args_parser.add_argument("-f")
    args_parser.add_argument("-d", nargs="*")
    main(vars(args_parser.parse_args()))
