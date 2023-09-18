import os
import sys
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def fopen(file_name: str, mode: str, str_text: str) -> object:
    source = open(file_name, mode)
    source.write(str_text)
    return source


def funct_create_file() -> None:
    file_path = create_path(["app"] + [""])

    if sys.argv.count("-d"):
        index = sys.argv.index("-d") + 1

        if sys.argv.count("-f"):
            index_f = sys.argv.index("-f")
            file_path += create_path(sys.argv[index:index_f] + [""])
        else:
            file_path += create_path(sys.argv[index:])
        os.makedirs(file_path, exist_ok=True)

    if sys.argv.count("-f"):
        index_f = sys.argv.index("-f") + 1
        file_path += create_path(sys.argv[index_f:])

        t_now = datetime.now()
        date = t_now.strftime("%Y-%m-%d %H:%M:%S")

        page_num = 1

        if os.path.exists(file_path):
            source_f = fopen(file_path, "a", f"\n{date}\n")
            line_cont = f"Another line{page_num}"
        else:
            source_f = fopen(file_path, "w", f"\n{date}\n")
            line_cont = f"Line{page_num}"
        if source_f:
            while True:
                input_text = input(f"Enter content line: {line_cont} ")

                if input_text != "stop":
                    source_f.write(f"{page_num} {line_cont} {input_text} \n")
                    page_num += 1
                else:
                    source_f.close()
                    break


funct_create_file()
