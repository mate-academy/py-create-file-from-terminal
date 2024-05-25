import sys
import os
import datetime


def main() -> None:
    commands = sys.argv
    if "-d" in commands:
        make_directory(commands)
    if "-f" in commands:
        filename = commands[commands.index("-f") + 1]
        create_file(filename)


def make_directory(commands: list) -> str | bytes:
    directories = []
    for directory in commands[commands.index("-d") + 1:]:
        if directory == "-f":
            break
        directories.append(directory)
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(filename: str) -> None:
    with open(filename, "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        line_number = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(str(line_number) + text + "\n")
            line_number += 1


if __name__ == "__main__":
    main()
