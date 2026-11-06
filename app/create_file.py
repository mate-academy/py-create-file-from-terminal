import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None
    current_flag = None

    for arg in args:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        else:
            if current_flag == "-d":
                dir_parts.append(arg)
            elif current_flag == "-f" and file_name is None:
                file_name = arg

    dir_path = ""
    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        content_lines = []

        while True:
            return_input = input("Enter content line: ")
            if return_input == "stop":
                break
            content_lines.append(return_input)

        file_path = os.path.join(dir_path, file_name)\
            if dir_path else file_name
        actual_time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_exists = os.path.exists(file_path)

        with open(file_path, "a", encoding="utf-8") as file:
            if file_exists:
                file.write("\n")

            file.write(f"{actual_time_stamp}\n")

            for index, line_content in enumerate(content_lines, start=1):
                file.write(f"{index} {line_content}\n")


create_file()
