import sys
import datetime
import os


def receive_data_from_cmd() -> list:
    return sys.argv[1:]


def receive_file_name(list_of_data: list) -> tuple:
    path_dir = None
    name_of_file = None
    if "-f" in list_of_data:
        f_index = list_of_data.index("-f")
        file_name_index = f_index + 1
        if f_index == -1:
            name_of_file = None
        elif list_of_data[f_index + 1] != "-d":
            name_of_file = list_of_data[file_name_index]
            list_of_data.pop(file_name_index)
            list_of_data.remove("-f")
    if "-d" in list_of_data and list_of_data.index("-d") != -1:
        d_index = list_of_data.index("-d")
        list_of_data.pop(d_index)
        path_dir = os.path.join(*list_of_data)
    return path_dir, name_of_file


def write_data(file_and_dir_name: tuple) -> None:
    dir_name, file_name = file_and_dir_name
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
        os.chdir(dir_name)
    if file_name:
        with open(file_name, "a", newline="", encoding="utf-8") as file:
            file.write(
                datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            content_line = input("Enter content line:")
            iteration = 0
            while content_line != "stop":
                iteration += 1
                file.write(f"{iteration} {content_line} \n")
                content_line = input("Enter content line:")
            file.write("\n")


row_data = receive_data_from_cmd()
file_and_path_name = receive_file_name(row_data)
write_data(file_and_path_name)
