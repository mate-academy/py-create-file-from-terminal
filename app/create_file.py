import sys
import os
from datetime import datetime
from typing import List, Optional


def parse_dirs(args: List[str]) -> List[str]:
    if "-d" not in args:
        return []

    idx: int = args.index("-d")
    dirs: List[str] = []

    for arg in args[idx + 1:]:
        if arg.startswith("-"):
            break
        dirs.append(arg)

    return dirs


def parse_filename(args: List[str]) -> Optional[str]:
    if "-f" not in args:
        return None

    idx: int = args.index("-f")
    if idx + 1 < len(args):
        return args[idx + 1]

    return None


def create_directories(dirs: List[str]) -> str:
    if not dirs:
        return ""

    path: str = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def write_file(path: str) -> None:
    file_exists: bool = os.path.exists(path)

    with open(path, "a") as f:
        if file_exists:
            f.write("\n\n")
        else:
            timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(timestamp + "\n")

        line_number: int = 1
        while True:
            line: str = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1


args: List[str] = sys.argv[1:]

dirs: List[str] = parse_dirs(args)
filename: Optional[str] = parse_filename(args)

dir_path: str = create_directories(dirs)

if filename is not None:
    full_path: str = os.path.join(dir_path, filename) if dir_path else filename
    write_file(full_path)
