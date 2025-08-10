import os
import sys
from datetime import datetime

args = sys.argv


def create_and_write_to_file(path_new_file: str) -> None:
    file_information = []

    while True:
        print("To finish, enter 'stop'.")
        info = input("Enter new line of content: ")
        if info.lower() == "stop":
            break
        file_information.append(info)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(path_new_file)

    with open(path_new_file, "a") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")
        for line_number, line in enumerate(file_information, 1):
            file.write(f"{line_number} {line}\n")

    print(f"File saved at: {path_new_file}")


def create_directory(*path_new_directory) -> None:
    destination = os.path.join(*path_new_directory)
    if not os.path.isdir(destination):
        os.makedirs(destination, exist_ok=True)
        print(f"Directory created: {destination}")
    else:
        print("Directory already exists")


if "-d" in args and "-f" in args:
    d_index = args.index("-d")
    f_index = args.index("-f")

    directories = args[d_index + 1:f_index]
    file_name = args[f_index + 1]

    create_directory(*directories)
    file_path = os.path.join(*directories, file_name)
    create_and_write_to_file(file_path)


elif "-d" in args and "-f" not in args:
    d_index = args.index("-d")
    directories = args[d_index + 1:]
    create_directory(*directories)

elif "-f" in args and "-d" not in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]
    create_and_write_to_file(file_name)
