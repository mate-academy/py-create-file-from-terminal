import sys
import os
from datetime import datetime


def main() -> None:
    parameters = sys.argv[1:]

    if "-d" in parameters and "-f" in parameters:
        d_index = parameters.index("-d")
        f_index = parameters.index("-f")
        directory_parts = (
            parameters[d_index + 1: f_index]
            if d_index < f_index
            else parameters[d_index + 1:]
        )

        file_name = parameters[f_index + 1]
        new_file_location = os.path.join(*directory_parts, file_name)
        create_directory(directory_parts)
        create_file(new_file_location)
    elif "-d" in parameters:
        create_directory(parameters[1:])
    elif "-f" in parameters:
        create_file(parameters[1])


def create_directory(path_parts: list[str]) -> None:
    dir_name = os.path.join(*path_parts)
    os.makedirs(dir_name, exist_ok=True)


def create_file(file_name: str) -> None:
    mode = "a" if os.path.exists(file_name) else "w"
    with open(file_name, mode) as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_num = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                file.write("\n")
                break
            file.write(f"{line_num} {text}\n")
            line_num += 1


if __name__ == "__main__":
    main()
