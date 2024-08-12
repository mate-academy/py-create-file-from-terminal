import sys
from datetime import datetime
from pathlib import Path


def create_directory(path: list) -> Path:
    directory = Path(*path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def write_to_the_file(file_name: str) -> None:
    counter = 0
    content = []
    while True:
        counter += 1
        new_line = input("Enter content line: ")
        if new_line == "stop":
            content.append("\n")
            break
        content.append(f"{new_line}\n")
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.writelines(content)


def create_file() -> None:
    file_name = ""
    arguments = sys.argv[1:]
    if "-d" in arguments and "-f" in arguments:
        for key, value in enumerate(arguments):
            if value == "-d":
                start = key
            elif value == "-f":
                end = key
        path_dir = create_directory(arguments[start + 1:end])
        file_name = path_dir / arguments[len(arguments) - 1]
    elif arguments[0] == "-f":
        file_name = arguments[1]
    elif arguments[0] == "-d":
        path_dir = create_directory(arguments[1:])
        file_name = path_dir / "file.txt"
    write_to_the_file(file_name)
