import datetime
import os
import sys


def main():
    args = sys.argv
    if "-d" in args and "-f" in args:
        path_list = args[2:-2]
        file_name = args[-1]
        new_path = create_new_path(path_list)
        new_dir_file = os.path.join(new_path, file_name)
        create_new_file(new_dir_file)
    if "-d" in args:
        create_new_path(args[2:])
    if "-f" in args:
        create_new_file(args[2])


def create_new_path(lst: list) -> str:
    new_path = os.path.join(*lst)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


def create_new_file(name: str):
    with open(name, "a") as new_file:
        timestamp = datetime.datetime.now()
        now_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(now_date + "\n")
        number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                new_file.write("\n")
                exit()
            else:
                new_file.write(f"{number} {line}\n")
                number += 1


if __name__ == '__main__':
    main()
