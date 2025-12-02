import sys
import datetime
import os


def receive_data_from_cmd() -> list:
    return sys.argv[1:]


def receive_file_name(list_of_data: list) -> tuple:
    path_dir = None
    name_of_file = None
    if "-f" in list_of_data:
        if len(list_of_data[list_of_data.index("-f") + 1:]) != 0:
            name_of_file = list_of_data[-1]
            list_of_data.pop(list_of_data.index("-f")+1)
        list_of_data.pop(list_of_data.index("-f"))
    else:
        name_of_file = None

        list_of_data.pop(-1)
        list_of_data.pop(-1)
    if "-d" in list_of_data:
        list_of_data.pop(0)
        path_dir = os.path.join(*list_of_data) \
            if len(list_of_data) != 0 else None
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
