import os
import sys
from datetime import datetime


def create_directories(path_parts: list[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1
        f.write("\n")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path_parts = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            dir_path_parts = args[d_index + 1:]
            file_name = None
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        dir_path_parts = []
    else:
        print("Invalid flags.")
        return

    if dir_path_parts:
        dir_path = create_directories(dir_path_parts)
    else:
        dir_path = "."

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
