import datetime
import os
import sys


args = sys.argv[1:]


def create_file(path: str = None) -> None:
    if path is not None:
        file_name = os.path.join(path, args[-1])
    else:
        file_name = f"{args[-1]}"
    with open(file_name, "a") as file:
        lines = [f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                lines.append("\n")
                break
            lines.append(f"{new_line}\n")
        file.writelines(lines)


if "-d" in args and "-f" not in args:
    path = os.path.join(*args[1:])
    os.makedirs(path, exist_ok=True)

elif "-d" in args and "-f" in args:
    path = os.path.join(*args[1:-2])
    os.makedirs(path, exist_ok=True)
    create_file(path)

elif "-f" in args:
    create_file()
