import os
import sys
from datetime import datetime


def create_path(*args) -> str:
    return str(os.path.join(*args))


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        now = datetime.now()
        str_now = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(str_now + "\n")
        line_num = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line_num} {user_input} \n")


def create_directory(path_list: list) -> None:
    path = create_path(os.getcwd(), *path_list)
    os.makedirs(path, exist_ok=True)


def main(list_argv: list) -> None:
    try:
        index_d = list_argv.index("-d")
    except ValueError:
        index_d = None

    try:
        index_f = list_argv.index("-f")
    except ValueError:
        index_f = None

    if index_d is not None:
        if index_f is not None:
            path = create_path(*list_argv[index_d + 1:index_f])
            create_directory(path)
            create_file(os.path.join(path, list_argv[index_f + 1]))
        else:
            path = create_path(*list_argv[index_d + 1:])
            create_directory(path)

    if index_f is not None:
        create_file(list_argv[index_f + 1])


if __name__ == "__main__":
    main(sys.argv[1:])
