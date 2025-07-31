import sys
import os
from datetime import datetime
from typing import List, Optional


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_content() -> List[str]:
    lines: List[str] = []
    counter: int = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter}: {line})")
        counter += 1
    return lines


def write_to_file(file_path: str) -> None:
    timestamp: str = get_timestamp()
    content: List[str] = get_content()
    with open(file_path, "a") as f:
        f.write(timestamp + "\n")
        for line in content:
            f.write(line + "\n")
        f.write("\n")


def main() -> None:
    args: List[str] = sys.argv[1:]
    if not args:
        print("Usage: create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    file_name: Optional[str] = None
    dir_parts: List[str] = []
    i: int = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                print("Error: No file name provided after -f")
                return
        else:
            print(f"Unknown flag or argument: {args[i]}")
            return

    dir_path: str = (
        os.path.join(os.getcwd(), *dir_parts) 
        if dir_parts 
        else os.getcwd()
    )

    if dir_parts:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        file_path: str = os.path.join(dir_path, file_name)
        write_to_file(file_path)
        print(f"Content written to: {file_path}")
    else:
        print("No file flag (-f) provided; only directories created.")

if __name__ == "__main__":
    main()

