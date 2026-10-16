import os
import sys
import datetime
from typing import TextIO


def write_file_content(output_file: TextIO) -> None:
    str_num = 1
    content_file = input("Enter content line: ")
    output_file.write(
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
    )
    while content_file != "stop":
        output_file.write(f"{str_num} {content_file}\n")
        content_file = input("Enter content line: ")
        str_num += 1


if "-d" in sys.argv and "-f" in sys.argv:
    if sys.argv.index("-f") < sys.argv.index("-d"):
        path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        os.makedirs(path, exist_ok=True)
        file_name = "".join(
            sys.argv[sys.argv.index("-f") + 1:sys.argv.index("-d")]
        )
        file_exists = os.path.exists(os.path.join(path, file_name))
        with open(os.path.join(path, file_name), "a") as file:
            if file_exists:
                file.write("\n")
            write_file_content(file)

    else:
        path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:
                                      sys.argv.index("-f")])
        os.makedirs(path, exist_ok=True)
        file_name = "".join(sys.argv[sys.argv.index("-f") + 1:])
        file_exists = os.path.exists(os.path.join(path, file_name))
        with open(os.path.join(path, file_name), "a") as file:
            if file_exists:
                file.write("\n")
            write_file_content(file)


elif "-d" in sys.argv and "-f" not in sys.argv:
    path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
    os.makedirs(path, exist_ok=True)


elif "-f" in sys.argv and "-d" not in sys.argv:
    file_name = "".join(sys.argv[sys.argv.index("-f") + 1:])
    file_exists = os.path.exists(file_name)
    with open(file_name, "a") as file:
        if file_exists:
            file.write("\n")
        write_file_content(file)
