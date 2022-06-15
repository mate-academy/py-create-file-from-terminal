import os
import sys
import datetime


def creating_path(ls: list) -> str:
    path = os.path.join(*ls)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def creating_file(file: str):
    with open(file, "a") as file:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_date + "\n")
        number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                exit()
            else:
                file.write(f"{number} {content}\n")
                number += 1


def main():
    terminal = sys.argv
    if "-d" in terminal and "-f" in terminal:
        path_list = terminal[2:-2]
        file = terminal[-1]
        path = creating_path(path_list)
        new_dir_file = os.path.join(path, file)
        creating_file(new_dir_file)
    if "-d" in terminal:
        creating_path(terminal[2:])
    if "-f" in terminal:
        creating_file(terminal[2])


main()
