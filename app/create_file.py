import sys
from os import path, makedirs
from datetime import datetime

DIR_FLAG = "-d"
FILE_FLAG = "-f"


def get_file_info() -> None:
    dirs_list = []
    file_name = ""

    if DIR_FLAG in sys.argv:
        dir_flag_idx = sys.argv.index(DIR_FLAG)
        dirs_list = (sys.argv[dir_flag_idx + 1:sys.argv.index(FILE_FLAG)]
                     if FILE_FLAG in sys.argv else sys.argv[dir_flag_idx + 1:])
    if FILE_FLAG in sys.argv:
        file_name = sys.argv[sys.argv.index(FILE_FLAG) + 1]

    full_file_path = path.join(*dirs_list, file_name)

    return (dirs_list, file_name, full_file_path)


def create_file() -> None:
    dirs_list, file_name, full_file_path = get_file_info()

    enter_pressed_times = 0
    if len(dirs_list) and not path.exists(path.join(*dirs_list)):
        makedirs(path.join(*dirs_list))

    if file_name:
        with open(full_file_path, "w") as source_file:
            current_date = datetime.now()
            formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
            source_file.write(f"{formatted_date}\n")
            while True:
                result = input("Enter content line: ")
                if result == "stop":
                    break

                enter_pressed_times += 1
                source_file.write(f"{enter_pressed_times} {result}\n")


create_file()
