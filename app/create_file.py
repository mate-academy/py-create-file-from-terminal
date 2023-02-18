from datetime import datetime
import os.path
import sys


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_file() -> None:
    content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    file_name = sys.argv[-1]
    line_number = 1
    while True:
        print_line = input("Enter content line: ")
        if print_line == "stop":
            content += "\n"
            break
        content += f"{line_number} {print_line}\n"
        line_number += 1

    with open(file_name, "a") as file_out:
        file_out.write(content)


def create_directory(file_name: str = None) -> None:
    if file_name:
        path = create_path(sys.argv[2:-2])
    else:
        path = create_path(sys.argv[2:])

    try:
        os.makedirs(path)
    except FileExistsError:
        return
    finally:
        if file_name:
            os.chdir(path)
            create_file()


if "-d" in sys.argv and "-f" not in sys.argv:
    create_directory()

if "-f" in sys.argv and "-d" not in sys.argv:
    create_file()

if "-d" in sys.argv and "-f" in sys.argv:
    create_directory(sys.argv[-1])
