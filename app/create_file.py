import os
import sys
from datetime import datetime


def create_dirs(path_parts: list) -> str:
    dir_path = os.path.join(*path_parts)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(dir_path: str, file_name: str) -> None:
    content = []
    file_path = os.path.join(dir_path, file_name)

    with open(file_path, "a") as file:
        while True:
            data_input = input("Enter content line: ")
            if data_input.strip().lower() == "stop":
                break
            content.append(data_input)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content_with_timestamp = [
            f"{timestamp}\n",
            *[f"{i + 1} {line}\n" for i, line in enumerate(content)]
        ]

        file.write("".join(content_with_timestamp))
        file.write("\n")


def main() -> None:
    if len(sys.argv) > 1:
        if "-d" in sys.argv:
            dir_index = sys.argv.index("-d")
            dir_path = create_dirs(sys.argv[dir_index + 1:sys.argv.index("-f")
                                   if "-f" in sys.argv else None])

            if "-f" in sys.argv:
                create_file(dir_path, sys.argv[sys.argv.index("-f") + 1])

        elif "-f" in sys.argv:
            create_file(".", sys.argv[sys.argv.index("-f") + 1])
