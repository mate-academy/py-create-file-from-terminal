import sys
import os
from datetime import datetime

terminal_data = sys.argv


def make_directories(dirs: list) -> None:
    return os.makedirs(os.path.join(*dirs), exist_ok=True)


def input_file_contents(path_name: str) -> None:
    with open(path_name, "a") as file:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(time_now)
        line_num = 0
        while True:
            line_num += 1
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n\n")
                break
            file.write(f"\n{line_num} {content}")


if "-d" in terminal_data and "-f" in terminal_data:
    d_flag_index = terminal_data.index("-d")
    f_flag_index = terminal_data.index("-f")
    if f_flag_index > d_flag_index:
        directories = terminal_data[2:-2]
        file_name = terminal_data[-1]
    else:
        directories = terminal_data[d_flag_index + 1:]
        file_name = terminal_data[2]

    make_directories(directories)
    joined_path = os.path.join(*directories, file_name)
    input_file_contents(joined_path)


elif "-d" in terminal_data:
    directories = terminal_data[2:]
    make_directories(directories)

elif "-f" in terminal_data:
    file_name = terminal_data[-1]
    input_file_contents(file_name)
