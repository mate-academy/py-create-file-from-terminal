import os
import sys
from datetime import datetime


def make_directory(directories: list) -> str | bytes:
    directory_part = os.path.join(*directories)
    os.makedirs(directory_part, exist_ok=True)
    return directory_part


def make_files(file_name: str, path: str = ".") -> None:
    file_path = os.path.join(file_name, path)
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %I:%M:%S") + "\n")
        line_add = 0
        while True:
            line_add += 1
            input_text_for_file = input("Enter content line: ")
            if input_text_for_file == "stop":
                file.write("\n")
                break
            file.write(f"{line_add} {input_text_for_file} ]n")


def main() -> None:
    input_flag = sys.argv
    if "-f" in input_flag:
        make_files(input_flag[-1])
    if "-d" in input_flag:
        make_files(input_flag[2:])
    if "-f" in input_flag and "-d" in input_flag:
        path = make_directory(input_flag[2: -2])
        make_files(input_flag[-1], path)


if __name__ == "__main__":
    main()
