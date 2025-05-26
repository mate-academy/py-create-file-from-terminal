import os
import sys
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def write_content(file_path: str) -> None:
    content = ""
    line_number = 0

    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")

    content += formatted + "\n"

    while True:
        line_number += 1
        line_input = input("Enter content line: ")
        if line_input.strip().lower() == "stop":
            break
        content += f"{line_number} {line_input}\n"

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content + "\n")


def main() -> None:
    args = sys.argv
    d_index = args.index("-d") if "-d" in args else -1
    f_index = args.index("-f") if "-f" in args else -1
    directories = args[d_index + 1 : f_index] if "-d" in args else []
    file_name = args[f_index + 1] if "-f" in args else None

    directory_path = create_path(directories)

    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        write_content(file_path)


if __name__ == "__main__":
    main()
