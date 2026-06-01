import sys
import os
from datetime import datetime


def create_directory(parts_directory: list[str]) -> str:
    dir_path = os.path.join(*parts_directory)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(
    file_name: str,
    parts_directory: list[str] = None
) -> None:
    content = []
    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break
        content.append(line)

    if parts_directory:
        dir_path = create_directory(parts_directory)
        filepath = os.path.join(dir_path, file_name)
    else:
        filepath = file_name

    filepath_exists = os.path.exists(filepath)
    if filepath_exists:
        timestamp = datetime.now().strftime("\n%Y-%m-%d %H:%M:%S")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as file_path:
        file_path.write(timestamp + "\n")
        for index, line_content in enumerate(content, start=1):
            file_path.write(f"{index} {line_content}\n")


def main() -> None:

    flags = sys.argv[1:]
    if "-d" in flags and "-f" in flags:
        d_index = flags.index("-d")
        f_index = flags.index("-f")
        if d_index < f_index:
            directory = flags[d_index + 1:f_index]
        else:
            directory = flags[d_index + 1:]
        filename = flags[f_index + 1]
        create_file(parts_directory=directory, file_name=filename)
    elif "-f" in flags:
        f_index = flags.index("-f")
        filename = flags[f_index + 1]
        create_file(file_name=filename)
    elif "-d" in flags:
        d_index = flags.index("-d")
        directory = flags[d_index + 1:]
        create_directory(directory)


main()
