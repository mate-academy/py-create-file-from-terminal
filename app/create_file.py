import sys
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    directories_list: list[str] = []
    file_name: str | None = None
    current_flag: str | None = None
    for arg in sys.argv[1:]:
        if arg == "-d":
            current_flag = "d"
            continue
        elif arg == "-f":
            current_flag = "f"
            continue

        if current_flag == "d":
            directories_list.append(arg)
        elif current_flag == "f":
            file_name = arg
    return directories_list, file_name


def create_directories(directories_list: list[str]) -> str:
    if directories_list:
        dir_path = os.path.join(*directories_list)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    return "."


def get_file_content() -> list[str]:
    content_lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    date_time = datetime.now().strftime("%Y-%m-%d %X")
    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(f"{date_time}\n")
        for numb, line in enumerate(content_lines, 1):
            file.write(f"{numb} {line}\n")


def main() -> None:
    directories_list, file_name = parse_arguments()
    dir_path = create_directories(directories_list)

    if file_name is not None:
        file_path = os.path.join(dir_path, file_name)
        content = get_file_content()
        write_to_file(file_path, content)
