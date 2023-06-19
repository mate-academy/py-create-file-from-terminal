from os import path, makedirs
from datetime import datetime
from sys import argv


def create_file(command: list) -> None:
    def create_directory(directories: list) -> None:
        dir_path = path.join(*directories)
        makedirs(dir_path, exist_ok=True)

    def write_into_file() -> None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")

        line_number = 1
        while True:
            line = input(
                "Enter new content line or 'stop' to end the program: "
            )
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
        file.write("\n")

    if ("-f" in command) and ("-d" in command):
        f_index = command.index("-f")
        file_name = command[-1]
        directory = command[1:f_index]
        create_directory(directory)
        with open(path.join(*directory, file_name), "a") as file:
            write_into_file()

    elif "-f" in command:
        file_name = command[-1]
        with open(file_name, "a") as file:
            write_into_file()

    elif "-d" in command:
        directory = command[1:]
        create_directory(directory)


if __name__ == "__main__":
    create_file(argv[1:])
