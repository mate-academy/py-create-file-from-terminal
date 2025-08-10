import sys
import os
from datetime import datetime
from typing import List, Optional, LiteralString


def create_directory(path_parts: List[str]) -> LiteralString | str | bytes:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, "a") as file:
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input("Enter content line (type 'stop' to finish): ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    dir_path: Optional[str] = None
    file_name: Optional[str] = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_args = []
        for i in range(d_index + 1, len(args)):
            if args[i] == "-f":
                break
            dir_args.append(args[i])

        if dir_args:
            dir_path = create_directory(dir_args)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        if not file_name:
            return

    if file_name:
        file_path = os.path.join(dir_path or "", file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
