from datetime import datetime
import os.path
import sys


def crate_file():
    # parsing args
    arguments = sys.argv
    dir_dict = []
    file_name = "default_name.txt"
    for index, arg in enumerate(arguments):
        if arg == "-d":
            for i in range(index + 1, len(arguments)):
                if arguments[i] == "-f":
                    break
                dir_dict.append(arguments[i])
        if arg == "-f":
            file_name = arguments[index + 1]

    # crating directories
    path = "\\".join(dir_dict)
    if path == "":
        path_file_name = file_name
    else:
        path_file_name = f"{path}\\{file_name}"
        os.makedirs(path, exist_ok=True)

    # writing info into a file
    num = 0
    with open(path_file_name, "a") as file:
        while True:
            if num == 0:
                dtn = datetime.now()
                file.write(f"{dtn.strftime('%Y.%m.%d %A %H:%M:%S')}\n")
            num += 1
            enter = input("Enter content line: ")
            if enter == "stop":
                break
            file.write(f"{num} {enter}\n")


if __name__ == "__main__":
    crate_file()
