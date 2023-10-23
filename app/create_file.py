from datetime import datetime
from os import makedirs, path
from sys import argv


def create_directory(directory: str) -> None:
    makedirs(directory)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        content = get_content()
        for line in content:
            file.write(line)
        file.write("\n")


def get_content() -> list:
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")]
    line_number = 1

    while True:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        content.append(f"{line_number} {new_line}\n")
        line_number += 1

    return content


def parse_command() -> None:
    user_command = argv
    file_name = ""
    directory_name = ""

    if "-f" in user_command:
        f_index = user_command.index("-f")
        file_name = user_command[f_index + 1]
        del user_command[f_index:f_index + 2]

    if "-d" in user_command:
        directory_name = path.join(*user_command[2:])

    if directory_name:
        create_directory(directory_name)

    if file_name:
        create_file(path.join(directory_name, file_name))


if __name__ == "__main__":
    parse_command()
