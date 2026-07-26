import datetime
import os
import sys


def handle_file(file_root):
    with open(f"{file_root}", "a") as file:
        counter = 1
        file.write(
            f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
        )

        while True:
            inputted_data = input("Enter content line: ")
            if inputted_data == "stop":
                break
            file.writelines(f"{counter} {inputted_data}\n")
            counter += 1
        file.write("\n")


def make_dir(dirs):
    path = os.path.join(*dirs)

    if not os.path.exists(path):
        os.makedirs(path)
    return path


def main():
    sys_argv = sys.argv

    if "-f" in sys_argv and "-d" in sys_argv:
        handle_file(f"{make_dir(sys_argv[2:-2])}{sys_argv[-1]}")
    elif "-f" in sys_argv:
        handle_file(f"{sys_argv[-1]}")
    elif "-d" in sys_argv:
        make_dir(sys_argv[2:])
