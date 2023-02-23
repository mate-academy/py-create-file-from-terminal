from datetime import datetime
import os.path
import sys


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_file() -> None:
    content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    line_number = 1
    with open(sys.argv[-1], "a") as file_out:
        file_out.write(content)
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file_out.write("\n")
                break
            file_out.write(f"{line_number} {content}\n")
            line_number += 1


def create_directory(file_name: str = None) -> None:
    if file_name:
        path = create_path(sys.argv[2:-2])
    else:
        path = create_path(sys.argv[2:])

    os.makedirs(path, exist_ok=True)

    if file_name:
        os.chdir(path)
        create_file()


if "-d" in sys.argv and "-f" not in sys.argv:
    create_directory()

if "-f" in sys.argv and "-d" not in sys.argv:
    create_file()

if "-d" in sys.argv and "-f" in sys.argv:
    create_directory(sys.argv[-1])

