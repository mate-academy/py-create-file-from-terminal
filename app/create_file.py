import os
import datetime
import sys


def create_dir(path_dir: str) -> None:
    if not os.path.exists(path_dir):
        os.makedirs(os.path.dirname(path_dir))


def create_file(file_name: str) -> None:
    file_attribute = "w"
    if os.path.exists(file_name):
        file_attribute = "a"
    with open(f"{file_name}", f"{file_attribute}") as file:
        i = 1
        now = datetime.datetime.now()
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"{i} {new_line} \n")
            i += 1
        file.write("\n")


def create_dir_and_file(command: list) -> None:
    file_name = command[-1]
    path_dir = ""
    if "-d" in command and "-f" in command:
        for i in command[2:-2]:
            path_dir += f"{i}/"
        create_dir(path_dir)
        create_file(path_dir + file_name)
    elif "-f" in command:
        create_file(file_name)
    elif "-d" in command:
        for i in command[2:]:
            path_dir += f"{i}/"
        create_dir(path_dir)


if __name__ == "__main__":
    create_dir_and_file(sys.argv)
