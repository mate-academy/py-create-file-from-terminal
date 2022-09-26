import argparse
import os
from datetime import datetime


def parse_commands() -> tuple[list, str]:
    parser = argparse.ArgumentParser(description="Create file from terminal.")
    parser.add_argument("-d", nargs="*", help="Directories to create.")
    parser.add_argument("-f", nargs="?", help="Name of file to create.")

    args = vars(parser.parse_args())

    return args["d"] or [], args["f"]


def create_directories(dirs: list[str]) -> None:
    if not dirs:
        return

    os.makedirs(os.path.join(*dirs), exist_ok=True)


def create_file(dirs: list[str], filename: str | None):
    if not filename:
        return

    with open(os.path.join(*dirs, filename), "a") as f:
        time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        lines = ""
        line_no = 1
        while (line := input("Enter content line: ")) != "stop":
            lines += f"{line_no} {line}\n"
            line_no += 1

        if lines:
            f.write(f"{time}\n{lines}\n")


def main() -> None:
    dirs, filename = parse_commands()
    create_directories(dirs)
    create_file(dirs, filename)


if __name__ == "__main__":
    main()
