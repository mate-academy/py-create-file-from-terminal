import sys
import os
import datetime


def main() -> None:
    commands = sys.argv
    path = ""
    if "-d" in commands:
        path = make_directory(commands)
    if "-f" in commands:
        filename = commands[commands.index("-f") + 1]
        create_file(filename, path)


def make_directory(commands: list) -> str:
    directories = []
    for directory in commands[commands.index("-d") + 1:]:
        if directory == "-f":
            break
        directories.append(directory)
    path = "/".join(directories) + "/"
    os.makedirs(path, exist_ok=True)
    return path


def create_file(filename: str, path:str) -> None:
    with open(path + filename, "a") as file:
        file.write(
            datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S") + "\n"
        )
        line_number = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                file.write("\n")
                break
            file.write(str(line_number) + text + "\n")
            line_number += 1


if __name__ == "__main__":
    main()
