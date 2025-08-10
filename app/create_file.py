import sys
import os
from datetime import datetime
from typing import List, Optional


def create_directory(path_parts: List[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Created directory: {path}")
    return path


def create_file_with_content(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_count = 1
        while True:
            line = input("Enter content line (or 'stop' to finish): ")
            if line.lower() == "stop":
                break
            file.write(f"{line_count} {line}\n")
            line_count += 1

    print(f"File '{file_path}' created or updated with content.")


def main() -> None:
    args = sys.argv[1:]
    if not args or "-d" not in args and "-f" not in args:
        print("Usage: python create_file.py [-d path] [-f file]")
        return

    directory_path: Optional[str] = None

    if "-d" in args:
        dir_index = args.index("-d") + 1
        path_parts = []
        while dir_index < len(args) and not args[dir_index].startswith("-"):
            path_parts.append(args[dir_index])
            dir_index += 1
        directory_path = create_directory(path_parts)
    else:
        directory_path = "."

    if "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index] if file_index < len(args) else None
        if file_name:
            file_path = os.path.join(directory_path, file_name)
            create_file_with_content(file_path)
        else:
            print("Error: no file name provided after '-f'.")
    else:
        print("Flag '-f' not provided, no file created.")


if __name__ == "__main__":
    main()
