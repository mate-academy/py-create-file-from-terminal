import sys
import os
from datetime import datetime


def create_file_with_data(file_name: str) -> None:
    parameter_to_open_file = "a" if os.path.isfile(file_name) else "w"
    with open(file_name, parameter_to_open_file) as file:
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_timestamp}\n")
        index = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{index} {line}\n")
            index += 1


def create_file() -> None:
    command_line = sys.argv[1:]
    if "-d" in command_line and "-f" not in command_line:
        path_dir = os.path.join(*command_line[1:])
        os.makedirs(path_dir, exist_ok=True)

    elif "-d" not in command_line and "-f" in command_line:
        file_name = command_line[1]
        create_file_with_data(file_name)

    elif "-d" in command_line and "-f" in command_line:
        path, file_name = " ".join(command_line).split("-f ")
        path_and_file_name = os.path.join(*path.split()[1:], file_name)

        path, file_name = os.path.split(path_and_file_name)
        os.makedirs(path, exist_ok=True)
        create_file_with_data(os.path.join(path, file_name))
    else:
        print("Expected '-d' or '-f'")
        return


if __name__ == "__main__":
    create_file()
