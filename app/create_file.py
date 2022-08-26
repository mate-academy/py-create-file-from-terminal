import sys
import os
import datetime


def create_file_from_terminal(path):
    create_dir = False
    create_file = False
    for text in path:
        if text == "-d":
            create_dir = True
        if text == "-f":
            create_file = True
    if create_dir:
        path_str = ""
        index = 0
        for txt in path:
            if txt == "-f":
                index = 0
            if index == 1:
                path_str += txt
                path_str += "/"
            if txt == "-d":
                index = 1
        path_str = path_str[:-1]
        os.makedirs(path_str)
        os.chdir(path_str)
    if create_file:
        file_name = path[-1]
        with open(file_name, "a") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            content = input("Enter content line:")
            while content != "stop":
                file.write("\n")
                file.write(content)
                content = input("Enter content line:")


if __name__ == "__main__":
    create_file_from_terminal(sys.argv)
