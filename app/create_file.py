import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv

    dirs = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")
            dirs = args[d_index + 1:f_index]
        else:
            dirs = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if dirs:
        path = os.path.join(*dirs)
    else:
        path = os.getcwd()

    if dirs:
        os.makedirs(path, exist_ok=True)

    if not file_name:
        print("File name not provided")
        return

    file_path = os.path.join(path, file_name)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as f:
        f.write(timestamp + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


if __name__ == "__main__":
    main()
