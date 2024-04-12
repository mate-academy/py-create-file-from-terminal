import os
import datetime
from sys import argv


def get_path(argv: list) -> (str, str):
    f_index = argv.index("-f") if "-f" in argv else ""
    d_index = argv.index("-d") if "-d" in argv else ""

    file_name = argv[-1] if f_index else ""

    if d_index and f_index:
        return os.path.join(*argv[d_index + 1:f_index]), file_name
    elif d_index:
        return os.path.join(*argv[d_index + 1:]), file_name

    return "", file_name


if __name__ == "__main__":
    dir_name, file_name = get_path(argv)
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    if file_name:
        with open(os.path.join(dir_name, file_name), "a") as new_file:
            new_file.write(current_date_time + "\n")
            while True:
                new_line = input("Enter content line: ")
                if new_line == "stop":
                    break
                new_file.write(new_line + "\n")
            new_file.write("\n")
