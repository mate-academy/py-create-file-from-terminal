import sys
from datetime import datetime
import os


def main_function(args: list[str]) -> None:
    dict_data = read_data(args)

    create_directories(dict_data["file_directories"])
    create_file(dict_data["file_directories"], dict_data["file_name"])


def create_directories(file_directory: str) -> None:
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)


def create_file(file_directory: str, file_name: str) -> None:
    if not file_name:
        return

    with open(os.path.join(file_directory, file_name), "a") as file:
        file.writelines(
            datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n"
        )
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.writelines(new_line + "\n")


def read_data(data: list[str]) -> dict:
    arguments_dict = {"file_name": "", "file_directories": os.getcwd()}
    i = 1
    while i < len(data):
        if data[i] == "-f":
            arguments_dict["file_name"] = data[i + 1]
            i += 1
        elif data[i] == "-d":
            i += 1
            while i < len(data) and data[i] != "-f":
                arguments_dict["file_directories"] = os.path.join(
                    arguments_dict["file_directories"], data[i]
                )
                i += 1
        else:
            i += 1
    return arguments_dict


if __name__ == "__main__":
    main_function(sys.argv)
