import sys
import os
from datetime import datetime


def parse_args() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index:f_index]
        else:
            dir_parts = args[d_index:]

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]

    return dir_parts, file_name


def create_directory(dir_parts: list[str]) -> str:
    if not dir_parts:
        return ""

    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(file_name: str, dir_path: str) -> None:
    full_file_path = (
        os.path.join(dir_path, file_name)
        if dir_path else file_name
    )

    with open(full_file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    dirs, filename = parse_args()
    dir_path = create_directory(dirs)
    print(f"Directory created at: {dir_path}")

    if filename:
        create_file(filename, dir_path)
