from sys import argv
from os import makedirs, path
from datetime import datetime


def create_directory(directories_path: list[str]) -> None:
    directories_path = path.join(*directories_path)
    makedirs(directories_path, exist_ok=True)


def create_file(file_name: str) -> None:
    date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_data = []

    while True:
        new_line = input("Enter content line: ")
        if new_line.strip().lower() == "stop":
            break
        file_data.append(new_line)

    with open(file_name, "a") as opened_file:
        opened_file.write(f"{date_today}\n")
        for i, line in enumerate(file_data):
            opened_file.write(f"{i + 1} {line}\n")
        opened_file.write("\n")


def create_file_from_terminal(commands: list) -> None:
    if not commands:
        raise ValueError("No command provided, such as '-f' or '-d'.")

    if "-d" in commands and "-f" in commands:
        d_index = commands.index("-d")
        f_index = commands.index("-f")

        if d_index > f_index:
            directory = commands[d_index + 1:]
        elif f_index > d_index:
            directory = commands[d_index + 1: f_index]
        file_name = commands[f_index + 1]
        file_path = path.join(*directory, file_name)
        create_directory(directory)
        create_file(file_path)

    elif "-d" in commands:
        d_index = commands.index("-d")
        create_directory(commands[d_index + 1:])

    elif "-f" in commands:
        f_index = commands.index("-f")
        create_file(commands[f_index + 1])


if __name__ == "__main__":
    create_file_from_terminal(argv[1:])

