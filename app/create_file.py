import sys
import os
from datetime import datetime


def create_file_in_path() -> None:
    file_name = ""
    path_list = []

    cl_input = sys.argv

    if "-f" in cl_input:

        try:
            file_name = (
                cl_input[cl_input.index("-f") + 1]
                if cl_input[cl_input.index("-f") + 1] != "-d"
                else ""
            )
        except IndexError:
            pass

    if "-d" in cl_input:
        for i in range(cl_input.index("-d") + 1, len(cl_input)):
            if cl_input[i] == "-f":
                break
            path_list.append(cl_input[i])

    if not file_name:
        if path_list:
            path = os.path.join(*path_list)
            if not os.path.exists(path):
                os.makedirs(path)
        return

    filepath = os.path.join(*path_list, file_name)
    with open(filepath, mode="a", newline="") as file:
        file.write(
            f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n"
            )
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{line_num} {line}\n")
            line_num += 1


if __name__ == "__main__":
    create_file_in_path()
