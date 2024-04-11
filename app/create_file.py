import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path)


def create_file(filename: str) -> None:
    with open(filename, "a") as f:
        count = 1
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            line_input = input("Enter content line: ")
            if line_input == "stop":
                break
            f.writelines(f"{count} {line_input}\n")
            count += 1
        f.write("\n")


if "-d" in sys.argv and "-f" in sys.argv:
    index_f = sys.argv.index("-f")
    directory_path = os.path.join(*sys.argv[2:index_f])
    create_directory(directory_path)
    create_file(os.path.join(directory_path, sys.argv[2]))

elif "-d" in sys.argv:
    create_directory(os.path.join(*sys.argv[2:]))

elif "-f" in sys.argv:
    create_file(sys.argv[2])
