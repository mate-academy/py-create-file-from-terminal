import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(filename: str, path: str = "") -> None:
    file_path = os.path.join(path, filename)
    is_new = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if is_new:
            file.write("\n\n")
        file.write(create_content())


def create_content() -> str:
    content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    line_count = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(f"{line_count} {line}")
        line_count += 1
    return "\n".join(content)


def main() -> None | str:
    input_data = sys.argv
    dirs = None
    file_name = None

    if "-d" in input_data:
        if "-f" in input_data:
            dirs = input_data[
                   input_data.index("-d") + 1: input_data.index("-f")
            ]
        else:
            dirs = input_data[input_data.index("-d") + 1:]

    if "-f" in input_data:
        if "-d" in input_data:
            file_name = input_data[
                        input_data.index("-f") + 1: input_data.index("-d")
            ]
        else:
            file_name = input_data[input_data.index("-f") + 1]

    if file_name:
        return create_file(file_name, create_path(dirs) if dirs else None)
    elif dirs:
        return create_path(dirs)


if __name__ == "__main__":
    main()
