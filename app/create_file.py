import sys
import os
from datetime import datetime


args = sys.argv[1:]


def create_file() -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    path = ""

    if "-d" in args:
        file_path = args[args.index("-d") + 1:]
        if "-f" in file_path:
            file_path = file_path[:file_path.index("-f")]
        path = os.path.join(*file_path)
        os.makedirs(path, exist_ok=True)

    if "-f" in args:
        name = args[args.index("-f") + 1]

        full_path = os.path.join(path, name) if path else name

        content = []

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break

            content.append(f"{len(content) + 1} {line}\n")

        mode = "a" if os.path.exists(full_path) else "w"

        with open(full_path, mode) as f:
            if mode == "a":
                f.write("\n")

            f.write(timestamp + "\n")
            f.writelines(content)


create_file()
