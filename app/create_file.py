import os
import sys
import datetime


def create_file_with_content(full_file_path: str) -> None:
    with open(full_file_path, "a") as new_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(timestamp + "\n")
        lines = []
        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            lines.append(user_input)

        for number, line in enumerate(lines, start=1):
            new_file.write(f"{number} {line}\n")
        new_file.write("\n")


def create_directories(dirs_list: list) -> str:
    dir_path = os.path.join(*dirs_list)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    return dir_path


module_args = sys.argv

d_index = module_args.index("-d") if "-d" in module_args else -1
f_index = module_args.index("-f") if "-f" in module_args else -1

if "-d" in module_args and "-f" in module_args:
    if d_index < f_index:
        dirs_list = module_args[d_index + 1:f_index]
        file_name = module_args[f_index + 1]
    else:
        file_name = module_args[f_index + 1]
        dirs_list = module_args[d_index + 1:f_index] \
            if f_index + 1 < d_index \
            else module_args[d_index + 1:]

    dir_path = create_directories(dirs_list)
    create_file_with_content(f"{dir_path}/{file_name}")

elif "-d" in module_args:
    dirs_list = module_args[d_index + 1:]
    create_directories(dirs_list)

elif "-f" in module_args:
    file_name = module_args[f_index + 1]
    create_file_with_content(file_name)
