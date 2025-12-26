from os import makedirs, getcwd, path

from sys import argv

from datetime import datetime


class CreateFileError(Exception):
    pass


def create_body_file(file_name: str) -> None:
    if path.getsize(file_name) == 0:
        body_file = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    else:
        body_file = ["\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    row_number = 0
    while True:
        line_file = input("Please input content lines: ")
        if line_file.lower() == "stop":
            break
        row_number += 1
        body_file.append(f"{row_number} {line_file}")
    with open(file_name, "a") as f:
        for line in body_file:
            f.write(line + "\n")


def command_processing(commands: list) -> list | str:
    command_line_args = commands
    if command_line_args[0] != "create_file.py":
        raise CreateFileError("Invalid input. Command must be create_file.py")
    elif not command_line_args[1:]:
        raise CreateFileError("Invalid input. "
                              "Command create_file.py is not enough")
    info_for_create_file = command_line_args[1:]
    if "-f" in info_for_create_file:
        if "file.txt" not in info_for_create_file:
            raise CreateFileError("Invalid input. "
                                  "Key -f is not possible without file")
        index_file = info_for_create_file.index("-f")
    else:
        index_file = len(info_for_create_file) + 1
    if "-d" in info_for_create_file:
        index_dir = info_for_create_file.index("-d")
        if "dir" not in info_for_create_file[index_dir + 1]:
            raise CreateFileError("Invalid input. "
                                  "Key -d is not possible without dir#")
        else:
            directories = info_for_create_file[index_dir + 1:index_file]
            base_path = getcwd()
            for directory in directories:
                new_path = path.join(base_path, directory)
                makedirs(new_path, exist_ok=True)
                base_path = new_path
    else:
        base_path = getcwd()
        index_dir = len(info_for_create_file) + 1
    return [base_path, index_dir, index_file, info_for_create_file]


def main() -> None:
    commands = argv
    base_path, index_dir, index_file, file_info = command_processing(commands)
    if "-f" in file_info and index_file < index_dir:
        create_body_file("file.txt")
    elif "-f" not in file_info or index_file > index_dir:
        full_path = path.join(base_path, "file.txt")
        create_body_file(full_path)


if __name__ == "__main__":
    main()
