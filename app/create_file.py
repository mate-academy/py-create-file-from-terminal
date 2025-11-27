import sys
import datetime
import os


def parse_args(argv: str = sys.argv[1:]) -> tuple:
    dirs = []
    i = 0

    filename = None
    while i < len(argv):
        if argv[i] == "-d":
            i += 1
            while i < len(argv) and argv[i] not in ("-d", "-f"):
                dirs.append(argv[i])
                i += 1
        elif argv[i] == "-f":
            i += 1
            if i < len(argv):
                filename = argv[i]
                i += 1
            else:
                raise ValueError("Missing filename after -f")

        else:
            raise ValueError(f"Unknown argument {argv[i]}")
    return dirs, filename


def read_lines() -> None:
    arguments = parse_args()
    filename = arguments[1]
    if not arguments[0]:
        target_dirs = os.path.join(*arguments[0])
    else:
        target_dirs = ""
    if target_dirs != "":
        os.makedirs(target_dirs, exist_ok=True)
    filepath = os.path.join(str(target_dirs), filename)
    line_number = 1

    with open(filepath, "a") as file:
        if os.path.exists(filepath):
            file.write("\n")
        now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write(now + "\n")
        print("Enter content line: (type stop to finish")

        while True:
            line = input()
            if line == "stop":
                break
            file.write(f"{line_number}. {line}\n")
            line_number += 1
