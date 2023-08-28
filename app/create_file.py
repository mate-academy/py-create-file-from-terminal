import getopt
import sys
import os
from datetime import datetime


def create_file(argv: list[str]) -> None:
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

    if dirpath != "":
        try:
            os.makedirs(os.path.join(*dirpath.split()))
        except FileExistsError:
            print("Directory already exists")

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


if __name__ == "__main__":
    create_file(sys.argv)
