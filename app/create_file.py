import sys
import os
import datetime

input_list = sys.argv[1:]

def find_pacth(find_list: list) -> str:
    patch = []
    if "-d" in find_list:
        d_index = find_list.index("-d")

        for i in range(d_index + 1, len(find_list)):
            if find_list[i] == "-f":
                break
            patch.append(find_list[i])

        folder_s_patch = os.path.join(*patch)
        return folder_s_patch


def find_name_file(find_list: list) -> str:
    f_index = find_list.index("-f")
    return find_list[f_index + 1]


def work_with_f(name_file: str) -> None:
    today = datetime.datetime.now()
    data_time = f"{today.date()} {today.hour}:{today.minute}:{today.second}"

    if not os.path.exists(name_file):
        with open(name_file, "w") as file:
            file.write(f"{data_time}\n")
    elif os.path.exists(name_file):
        with open(name_file, "a") as file:
            file.write(f"\n{data_time}\n")

    while True:
        line = str(input("Enter content line: "))
        if line == "stop":
            break
        with open(name_file, "a") as file:
            file.write(f"{line}\n")


if "-d" in input_list:
    if "-f" not in input_list:
        patch = find_pacth(input_list)
        os.makedirs(patch, exist_ok=True)

if "-f" in input_list:
    if "-d" not in input_list:
        work_with_f(find_name_file(input_list))

if "-f" in input_list:
    if "-d" in input_list:
        patch = find_pacth(input_list)
        os.makedirs(patch, exist_ok=True)
        file_patch = os.path.join(patch, find_name_file(input_list))

        work_with_f(file_patch)