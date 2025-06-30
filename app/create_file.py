import datetime
import os
import sys
from typing import List


def create_directory(directory_path: List[str]) -> str:
    path = os.path.join(*directory_path)
    os.makedirs(path, exist_ok=True)
    return path


def create_file() -> None:
    args = sys.argv[1:]
    path = ""

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []
        for i in range(d_index + 1, len(args)):
            if args[i] == "-f":
                break
            dir_parts.append(args[i])
        path = create_directory(dir_parts)

    if "-f" in args:
        f_index = args.index("-f")
        filename = args[f_index + 1]
        filepath = os.path.join(path, filename) if path else filename

        with open(filepath, "a") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            line = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                file.write(f"{line} {content}\n")
                line += 1


if __name__ == "__main__":
    create_file()
