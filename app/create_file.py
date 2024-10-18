import os
import sys
from datetime import datetime
from typing import List, Optional, LiteralString


def create_directory(path_parts: List[str]) -> LiteralString | str | bytes:
    # noinspection PyArgumentList
    path = os.path.join(*(str(part) for part in path_parts))
    os.makedirs(path, exist_ok=True)
    print(f"Directory {path} created.")
    return path


def create_file_with_content(file_path: str) -> None:
    content: List[str] = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        if mode == "w":
            file.write(f"{timestamp}\n")
            print(f"File {file_path} created.")
        else:
            file.write(f"\n{timestamp}\n")
            print(f"Appending content to existing file: {file_path}")

    line_num: int = 1
    while True:
        line: str = input(
            f"Enter content line ({line_num}, type 'stop' to finish): "
        )
        if line.lower() == "stop":
            break
        content.append(f"{line_num} {line}")
        line_num += 1

    with open(file_path, "a") as file:
        file.write("\n".join(content) + "\n")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py [-d directories] [-f filename]")
        return

    args: List[str] = sys.argv[1:]
    dir_parts: List[str] = []
    file_name: Optional[str] = None

    if "-d" in args:
        d_index: int = args.index("-d")
        dir_parts = args[
            d_index + 1:args.index("-f")] \
            if "-f" in args else args[d_index + 1:]

    if "-f" in args:
        f_index: int = args.index("-f")
        file_name = args[f_index + 1]

    # noinspection PyTypeChecker
    full_dir_path: str = create_directory(dir_parts)\
        if dir_parts else os.getcwd()
    if file_name:
        file_path: str = os.path.join(full_dir_path, file_name)
        create_file_with_content(file_path)


if __name__ == "__main__":
    main()
