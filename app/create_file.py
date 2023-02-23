import sys
from datetime import datetime
import os


def create_file(name: str, path: str = "") -> None:
    content = []

    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content.append(content_line)

    with open(path + name, "a") as file:
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(formatted_now + "\n")
        line_counter = 1
        if len(content) != 0:
            for line in content:
                file.write(f"{line_counter} " + line + "\n")
                line_counter += 1
            file.write("\n\n")


def create_directory(path_list: str) -> None:
    directories = path_list.split()
    print(directories)
    path = os.path.join(*directories)
    os.makedirs(path)


temp_list = sys.argv

if "-d" in temp_list:
    directory_path = " ".join(temp_list[1:])
    print(directory_path)
    if "-f" in directory_path:
        file_name = directory_path.split("-f")[1]
        directory_path = directory_path.split("-f")[0]
        directory_path = directory_path.split("-d")[1]
        create_directory(directory_path)
        directory_path = directory_path.split()
        path_for_file = "/".join(directory_path)
        path_for_file += "/"
        create_file(file_name, path_for_file)
if "-f" in temp_list and "-d" not in temp_list:
    directory_path = " ".join(temp_list[1:])
    file_name = directory_path.split("-f")[1]
    create_file(file_name)
