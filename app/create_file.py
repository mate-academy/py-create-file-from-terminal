import getopt
import sys
import os
from datetime import datetime


def parse_options(argv: list[str]) -> tuple[str, str]:
    try:
        opts, _ = getopt.getopt(argv[1:], "d:f:", [])
    except getopt.GetoptError as e:
        print(f"Exception: {e}")
        sys.exit(2)

    dirpath: str = ""
    filename: str = ""
    for opt, arg in opts:
        if "-d" == opt:
            dirpath = arg
        elif "-f" == opt:
            filename = arg
    return dirpath, filename


def make_directory(dirpath: str) -> None:
    if dirpath != "":
        try:
            os.makedirs(os.path.join(*dirpath.split()))
        except FileExistsError:
            print("Directory already exists")


def write_file(dirpath: str, filename: str) -> None:
    if filename != "":
        lines: list[str] = []
        line_number: int = 1
        while (line := input("Enter content line: ")) != "stop":
            lines.append(f"{line_number} {line}\n")
            line_number += 1
        with open(os.path.join(dirpath, filename), "a") as fobj:
            fobj.write(
                datetime.now().strftime("%Y-%M-%d %H:%M:%S\n")
                + "".join(lines)
                + "\n"
            )


def create_file(dirpath: str, filename: str) -> None:
    make_directory(dirpath)
    write_file(dirpath, filename)


if __name__ == "__main__":
    dirpath, filename = parse_options(sys.argv)
    create_file(dirpath, filename)
