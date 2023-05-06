from datetime import datetime
import os
import sys


def parsing_parameters() -> tuple:
    dir_list = []
    full_file_name = ""
    if "-f" in sys.argv and "-d" in sys.argv:
        full_file_name = sys.argv[sys.argv.index("-f") + 1]
        dir_list = sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
    elif "-f" in sys.argv:
        full_file_name = sys.argv[sys.argv.index("-f") + 1]
    elif "-d" in sys.argv:
        dir_list = sys.argv[sys.argv.index("-d") + 1:]
    return "/".join(dir_list), full_file_name


def make_directories(directories: str) -> None:
    if len(directories) > 0:
        os.makedirs(os.path.join(directories), exist_ok=True)


def create_file_with_content(name: str, content_path: str = "") -> None:
    if len(name) == 0:
        return
    path_with_file = os.path.join(content_path, name)
    first_symbol = "\n" if os.path.exists(path_with_file) else ""
    with open(path_with_file, "a") as file:
        # add current timestamp
        time_format = "%Y-%m-%d %H:%M:%S"
        file.write(
            f"{first_symbol + str(datetime.now().strftime(time_format))}\n"
        )

        # add content lines
        content = None
        row_number = 1
        while content != "stop":
            content = input("Enter content line: ")
            if content != "stop" and content is not None:
                file.write(f"{str(row_number)} {content}\n")
                row_number += 1


if __name__ == "__main__":
    path, file_name = parsing_parameters()
    make_directories(path)
    create_file_with_content(file_name, path)
