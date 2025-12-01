import sys
import datetime
import os


def parse_args(argv: list = None) -> tuple:
    if argv is None:
        argv = sys.argv[1:]
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
    dirs = arguments[0]
    filename = arguments[1]
    if filename is None:
        target_dirs = os.path.join(*dirs)
        os.makedirs(target_dirs, exist_ok=True)
        sys.exit()
    if dirs:
        target_dirs = os.path.join(*dirs)
        os.makedirs(target_dirs, exist_ok=True)
        filepath = os.path.join(target_dirs, filename)
    else:
        filepath = os.path.join(".", filename)
    line_number = 1
    existing_file = 0
    if os.path.exists(filepath):
        existing_file = 1
    with open(filepath, "a") as file:
        if existing_file == 1:
            file.write("\n")
        now = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write(now + "\n")
        print("Enter content line:")
        while True:
            line = input()
            if line == "stop":
                break
            file.write(f"{line_number}. {line}\n")
            line_number += 1


if __name__ == "__main__":
    read_lines()
