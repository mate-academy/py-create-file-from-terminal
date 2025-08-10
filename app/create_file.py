from os import path, makedirs
from datetime import datetime
from sys import argv


def create_file(command: list) -> None:
    def create_directory(directories: list) -> None:
        dir_path = path.join(*directories)
        makedirs(dir_path, exist_ok=True)

    def write_into_file(file_path: str | list) -> None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"{current_time}\n"

        line_number = 1
        while True:
            line = input(
                "Enter new content line or 'stop' to end the program: "
            )
            if line.lower() == "stop":
                break
            content += f"{line_number} {line}\n"
            line_number += 1

        with open(file_path, "a") as file:
            file.write(f"{content}\n")

    if ("-f" in command) and ("-d" in command):
        file_name = argv.pop(argv.index("-f") + 1)
        argv.pop(argv.index("-f"))
        directory = argv[argv.index("-d") + 1:]

        create_directory(directory)
        dir_path = path.join(*directory, file_name)
        write_into_file(dir_path)

    elif "-f" in command:
        file_name = argv.pop(argv.index("-f") + 1)
        write_into_file(file_name)

    elif "-d" in command:
        directory = argv[argv.index("-d") + 1:]
        create_directory(directory)


if __name__ == "__main__":
    create_file(argv[1:])
