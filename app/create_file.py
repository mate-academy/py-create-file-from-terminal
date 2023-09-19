import os
import sys
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def write_text_content(f_sourse: object,
                       page_num: int, line_cont: str) -> None:
    while True:
        input_text = input(f"Enter content line: {line_cont} ")

        if input_text == "stop":
            break
        f_sourse.write(f"{page_num} {line_cont} {input_text} \n")
        page_num += 1


def create_dir(file_path: list) -> None:
    page = file_path[0].split("/")[0]
    index_d = file_path.index("-d") + 1
    file_path = create_path([page] + file_path[index_d:])

    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)


def create_file(file_path: list) -> None:
    page = file_path[0].split("/")[0]
    index_f = file_path.index("-f")

    path1 = file_path[2:index_f]
    path2 = file_path[index_f + 1:]
    path = path1 + path2
    file_path = create_path([page] + path)
    page_num = 1

    if os.path.exists(file_path):
        with open(file_path, "a") as f:
            f.write(f"\n{current_date}\n")
            write_text_content(f, page_num, "Another")
    else:
        with open(file_path, "w") as f:
            f.write(f"\n{current_date}\n")
            write_text_content(f, page_num, "Line ")


current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def funct_create_file_from_terminal() -> None:
    list_avrg = sys.argv

    if sys.argv.count("-d") and sys.argv.count("-f") == 0:
        create_dir(list_avrg)

    if sys.argv.count("-f") and sys.argv.count("-d") == 0:
        create_file(list_avrg)

    if sys.argv.count("-d") and sys.argv.count("-f"):
        path_dir = list_avrg[:list_avrg.index("-f")]
        create_dir(path_dir)
        create_file(list_avrg)


funct_create_file_from_terminal()
