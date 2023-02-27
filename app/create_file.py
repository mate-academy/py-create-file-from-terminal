import sys

import os

from datetime import datetime

def create_file(name: str, path: str = "") -> None:
    path_file = name
    if path != "":
        path_file = os.path.join(path + "/" + name)

    with open(path_file, "a") as file:

        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(formatted_now + "\n")

        line_counter = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                break

            file.write(f"{line_counter} " + content_line + "\n")
            line_counter += 1
        file.write("\n\n")


def create_directory(path_list: str) -> None:
    directories = path_list.split()
    return os.makedirs(os.path.join(*directories), exist_ok=True)


def action(action_list: list) -> None:
    if "-d" in action_list:
        directory_path = " ".join(action_list[2:])
        create_directory(directory_path.split("-f")[0])

        if "-f" in directory_path:
            directory_path, file_name = directory_path.split("-f")

            create_directory(directory_path)

            directory_path = directory_path.split()
            path_for_file = os.path.join(*directory_path)
            create_file(file_name, path_for_file)

    if "-f" in action_list and "-d" not in action_list:
        directory_path = " ".join(action_list[1:])
        file_name = directory_path.split("-f")[1]
        create_file(file_name)


if __name__ == "__main__":
    temp_list = sys.argv

    action(temp_list)
