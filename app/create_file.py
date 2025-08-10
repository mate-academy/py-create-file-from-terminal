import sys
import os
from datetime import datetime
from typing import List, Optional


def create_directory(path_parts: List[str]) -> str:
    path: str = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")
    return path


def write_to_file(file_path: str) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists: bool = os.path.exists(file_path)

    with open(file_path, "a" if file_exists else "w", encoding="utf-8") as f:
        if file_exists:
            f.write("\n\n")
        f.write(f"{timestamp}\n")

        line_number: int = 1
        while True:
            content: str = input("Enter content line: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1

    print(f"File saved: {file_path}")


def main() -> None:
    args: List[str] = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [dir_path] -f [file_name]")
        return

    directory_parts: List[str] = []
    file_name: Optional[str] = None

    i: int = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                directory_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    if not file_name and not directory_parts:
        print("Error: No valid options provided")
        return

    directory_path: str = os.getcwd()

    if directory_parts:
        directory_path = create_directory(directory_parts)

    if file_name:
        file_path: str = os.path.join(directory_path, file_name)
        write_to_file(file_path)


if __name__ == "__main__":
    main()
