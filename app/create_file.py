import os
import sys
import datetime


def create_directory(dir_path: str, filename: str = None) -> None:
    dir_path = dir_path.split(" ")
    directory = []
    flag = False
    for word in dir_path:
        if word == "-f":
            directory.append(filename)
            create_file(os.path.join(*directory))
            break
        if flag:
            directory.append(word)
            os.mkdir(os.path.join(*directory))
        if word == "-d":
            flag = True


def create_file(file_name: str) -> None:
    with open(os.path.join(file_name), "a") as file:
        command = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(command + "\n")
        while True:
            command = input("Enter content line: ")
            if command == "stop":
                break
            file.write(command + "\n")
        file.write("\n")


sys_argv = " ".join(sys.argv)
sys_argv_last = sys.argv[-1]
if len(sys.argv) > 1 and "-d" in sys.argv and "-f" in sys.argv:
    create_directory(sys_argv, sys_argv_last)

elif len(sys.argv) > 1 and "-d" in sys.argv:
    create_directory(sys_argv)

elif len(sys.argv) > 1 and "-f" in sys.argv:
    create_file(sys_argv_last)
