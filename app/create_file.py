import os
import sys
from datetime import datetime


def create_directory(path_parts: list[str]) -> None:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)


def create_file(file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, "a" if os.path.exists(file_name) else "w") as file:
        file.write(f"{timestamp}\n")
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)
        for line_index, line in enumerate(content_lines, start=1):
            file.write(f"{line_index} {line}\n")


def main() -> None:
    cmd_line = sys.argv

    if "-d" in cmd_line and "-f" in cmd_line:
        directory_index = cmd_line.index("-d") + 1
        file_index = cmd_line.index("-f") + 1

        file_name = cmd_line[file_index]
        directory_path_parts = cmd_line[directory_index:]

        if directory_index < file_index:
            directory_path_parts = cmd_line[directory_index : file_index - 1]

        create_directory(directory_path_parts)
        os.chdir(os.path.join(*directory_path_parts))
        create_file(file_name)

    if "-d" in cmd_line and "-f" not in cmd_line:
        directory_index = cmd_line.index("-d") + 1
        directory_path_parts = cmd_line[directory_index:]
        create_directory(directory_path_parts)

    if "-f" in cmd_line and "-d" not in cmd_line:
        file_index = cmd_line.index("-f") + 1
        file_name = cmd_line[file_index]
        create_file(file_name)


if __name__ == "__main__":
    main()
