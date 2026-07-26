import os
import sys
from datetime import datetime


def create_file() -> None:
    directories = []
    filename = None
    if "-d" in sys.argv:
        index_d = sys.argv.index("-d")
        for i in range(index_d + 1, len(sys.argv)):
            if sys.argv[i].startswith("-"):
                break
            directories.append(sys.argv[i])
    if "-f" in sys.argv:
        filename_index = sys.argv.index("-f")
        filename = sys.argv[filename_index + 1]
    if filename is None:
        return
    if directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, filename)
    else:
        full_path = filename

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    with open(full_path, "a", encoding="utf-8") as f:
        f.write(timestamp + "\n")
        for i, text in enumerate(lines, start=1):
            f.write(f"{i} {text}\n")
        f.write("\n")


if __name__ == "__main__":
    create_file()
