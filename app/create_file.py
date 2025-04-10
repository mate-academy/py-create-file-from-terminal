import sys
import os
import datetime


def write_in_file(file_name: str) -> None:

    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, mode) as file:
        if mode == "a":
            file.write(f"\n\n{date_now}")
        else:
            file.write(date_now)

        str_num = 1

        while True:
            text_line = input("Enter content line: ")

            if text_line.lower() == "stop":
                break
            file.write(f"\n{str_num} {text_line}")

            str_num += 1


def reader_argv(paths: list) -> None:

    if "-d" in paths:
        d_index = paths.index("-d")
        dir_parts = []
        for path in paths[d_index + 1:]:
            if path.startswith("-"):
                break
            dir_parts.append(path)
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    if "-f" in paths:
        f_index = paths.index("-f")
        file_name = paths[f_index + 1]

        file_path = os.path.join(dir_path, file_name)
        write_in_file(file_path)


reader_argv(sys.argv)
