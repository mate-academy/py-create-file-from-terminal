import datetime
import sys
import os


def create_dir(dir_path: str):
    os.makedirs(dir_path)
    os.chdir(dir_path)


def create_file(filename: str):
    with open(filename, "a") as file:
        content = str(datetime.datetime.today()) + "\n"
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content += line + "\n"
        file.write(content)


if __name__ == "__main__":
    command = sys.argv
    current_dir = os.getcwd()
    if "-d" in command:
        if "-f" in command:
            new_dirs = command[command.index("-d"): -2]
            path = os.path.join(current_dir, *new_dirs)
            create_dir(path)
        else:
            new_dirs = command[command.index("-d"):]
            path = os.path.join(current_dir, *new_dirs)
            create_dir(path)
    if "-f" in command:
        create_file(command[-1])
