from datetime import datetime

import os
import sys


def main(all_command: list) -> None:
    new_way = ""
    for info in all_command[1:]:
        new_way += info + "/"
    if "-d" in new_way and "-f" in new_way:
        directory_way = new_way[new_way.find("d") + 2: new_way.rfind("-")]
        file_name = new_way[new_way.find("-f") + 3: -1]
        create_file_and_dirs(file_name, directory_way)
    if "-f" in new_way and "-d" not in new_way:
        file_name = new_way[new_way.find("f") + 2: -1]
        create_only_file(file_name)
    if "-d" in new_way and "-f" not in new_way:
        directory_way = new_way[new_way.find("-d") + 3: -1]
        create_only_dirs(directory_way)


def create_file_and_dirs(file_name: str,
                         directory_way: str) -> None:
    os.makedirs(directory_way, exist_ok=True)
    with open(os.path.join(directory_way, file_name), "a") as file_to_write:
        now = datetime.now()
        file_to_write.write(now.strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        some_content = input("Enter content line: ")
        while some_content != "stop":
            file_to_write.write(some_content + "\n")
            some_content = input("Enter content line: ")


def create_only_file(file_name: str) -> None:
    with open(file_name, "a") as file_to_write:
        now = datetime.now()
        file_to_write.write(now.strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        some_content = input("Enter content line: ")
        while some_content != "stop":
            file_to_write.write(some_content + "\n")
            some_content = input("Enter content line: ")


def create_only_dirs(dir_way: str) -> None:
    os.makedirs(os.path.join(dir_way), exist_ok=True)


if __name__ == "__main__":
    main(sys.argv)
