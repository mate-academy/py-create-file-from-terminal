import sys
import os
import datetime


class Flagerror(Exception):
    pass


class LenError(Exception):
    pass


input_list = sys.argv[1:]
if "-d" not in input_list and "-f" not in input_list:
    raise Flagerror("Flags not found")
if len(input_list) == 1:
    raise LenError("Found only flag")


def build_path(find_list: list) -> str:
    patch = []
    if "-d" in find_list:
        d_index = find_list.index("-d")

        for i in range(d_index + 1, len(find_list)):
            if find_list[i] == "-f":
                break
            patch.append(find_list[i])

        if not patch:
            raise ValueError("No directory components specified after -d")

        folder_s_patch = os.path.join(*patch)
        return folder_s_patch


def find_name_file(find_list: list) -> str:
    f_index = find_list.index("-f")
    if f_index == len(find_list) - 1:
        raise ValueError("File name not specified after -f flag")
    return find_list[f_index + 1]


def work_with_f(name_file: str) -> None:

    today = datetime.datetime.now()
    data_to_write = today.strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(name_file):
        with open(name_file, "w") as file:
            file.write(f"{data_to_write}\n")
    elif os.path.exists(name_file):
        with open(name_file, "a") as file:
            file.write(f"\n{data_to_write}\n")

    lines_to_write = []
    number_string = 1
    while True:
        line = str(input("Enter content line: "))
        if line == "stop":
            with open(name_file, "a") as file:
                file.writelines(lines_to_write)
            break
        lines_to_write.append(f"{number_string} {line}\n")
        number_string += 1


if "-d" in input_list:
    if "-f" not in input_list:
        patch = build_path(input_list)
        if not patch:
            raise ValueError("No valid directory path provided after -d")
        os.makedirs(patch, exist_ok=True)

if "-f" in input_list:
    if "-d" not in input_list:
        work_with_f(find_name_file(input_list))

if "-f" in input_list:
    if "-d" in input_list:
        dir_components = build_path(input_list)
        if not dir_components:
            raise ValueError("No directory components provided after -d")
        os.makedirs(dir_components, exist_ok=True)
        file_patch = os.path.join(dir_components, find_name_file(input_list))

        work_with_f(file_patch)
