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
                lines.append("\n")
                break
            lines.append(f"{str(num_line)} {new_line}\n")
            num_line += 1

        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

        file.write(date_str)
        file.writelines(lines)


def create_file() -> None:
    arr = sys.argv

    file_name = get_file_name(arr)
    dir_path = os.path.join(*get_dirs(arr))

    os.makedirs(dir_path, exist_ok=True)

    if file_name != "":
        write_content_to_file(os.path.join(dir_path, file_name))


create_file()
