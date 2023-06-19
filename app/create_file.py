from os import path, makedirs
from datetime import datetime


def create_file(command: str) -> None:
    def create_directory(directories: list) -> None:
        dir_path = path.join(*directories)
        makedirs(dir_path, exist_ok=True)

    def write_into_file() -> None:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")

        line_number = 1
        while True:
            line = input("Enter new content line or 'stop' to end the program: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1

    if ("-f" in command) and ("-d" in command):
        f_index = command.find("-f")
        file_name = command[f_index + 3:]
        directory = command[3:f_index]
        create_directory(directory.split())
        with open(path.join(*directory.split(), file_name), "w") as file:
            write_into_file()

    elif command.startswith("-f "):
        file_name = command[3:]
        with open(file_name, "w") as file:
            write_into_file()

    elif command.startswith("-d "):
        directory = command[3:]
        create_directory(directory.split())

if __name__ == "__main__":
    create_file(input("Enter the command: "))
