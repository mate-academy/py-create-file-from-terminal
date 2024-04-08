import sys
import os
from datetime import datetime


def create_dir(path: any) -> None:

    if not path:
        return
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print(f"Error creating directory {path}: {error}")


def create_file(path: any, file_name: str) -> None:

    full_path = os.path.join(path, file_name) if path else file_name

    file_exists = os.path.exists(full_path)

    with open(full_path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_count = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{line_count} {content_line}\n")
            line_count += 1


def main() -> None:
    args = sys.argv[1:]
    path_parts = []
    file_name = ""
    dir_flag = False
    file_flag = False
    parsing_dirs = False

    for arg in args:
        if arg == "-d":
            dir_flag = True
            parsing_dirs = True
        elif arg == "-f":
            file_flag = True
            parsing_dirs = False
        elif parsing_dirs:
            path_parts.append(arg)
        elif file_flag and not file_name:
            file_name = arg

    path = os.path.join(*path_parts) if path_parts else ""

    if dir_flag:
        create_dir(path)
    if file_flag:
        create_file(path, file_name)


if __name__ == "__main__":
    main()
