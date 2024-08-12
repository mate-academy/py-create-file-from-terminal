import os
import sys
import datetime


def get_dirs(terminal_req_arr: list) -> list:
    if "-d" not in terminal_req_arr:
        return []

    dir_list = []
    for dir_name in terminal_req_arr[terminal_req_arr.index("-d") + 1:]:
        if dir_name[0] == "-":
            break
        dir_list.append(dir_name)

    return dir_list


def get_file_name(terminal_req_arr: list) -> str:
    if "-f" not in terminal_req_arr:
        return ""

    return terminal_req_arr[-1]


def write_content_to_file(path: str) -> None:
    with open(path, "a+") as file:
        lines = []
        num_line = 1
        while True:

            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            lines.append(f"{str(num_line)} {new_line}\n")
            num_line += 1

        file.seek(0)
        content = file.read()
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

        if content:
            date_str = "\n" + date_str

        file.write(date_str)
        file.writelines(lines)


def create_file() -> None:
    arr = sys.argv

    file_name = get_file_name(arr)
    dir_path = "/".join(get_dirs(arr))

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if file_name == "":
        return

    write_content_to_file(f"{dir_path}/{file_name}")


create_file()
