import sys
import os
from datetime import datetime


def create_file_in_path() -> None:
    file_name = ""
    path_list = []

    cl_input = sys.argv

    if "-f" in cl_input:
        file_name = cl_input[cl_input.index("-f") + 1]
        f_index = cl_input.index("-f")

    if "-d" in cl_input:
        d_index = cl_input.index("-d")
        path_list = (
            cl_input[d_index + 1:]
            if "-f" not in cl_input
            else cl_input[d_index + 1:f_index]
        )

    if path_list:
        path = os.path.join(*path_list)
        os.makedirs(path, exist_ok=True)

    if not file_name:
        return

    filepath = os.path.join(*path_list, file_name)
    with open(filepath, mode="a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
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
