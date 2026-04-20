import sys
import os
from datetime import datetime
from typing import List

directories: List[str] = []
file_name: List[str] = []
dir_path: str = ""
content: List[str] = []


def parse_arguments(args: List[str]) -> None:
    global directories, file_name
    directories = []
    file_name = []
    checker_d = False
    checker_f = False

    for arg in args:
        if arg == "-d":
            checker_d = True
            checker_f = False
            continue
        if arg == "-f":
            checker_f = True
            checker_d = False
            continue
        if checker_d:
            directories.append(arg)
        if checker_f:
            file_name.append(arg)


def create_directories() -> None:
    global dir_path
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."


def collect_content() -> None:
    global content
    content = []
    while True:
        line = input("Enter content line: ").strip()
        if line.lower() == "stop":
            break
        content.append(line)


def write_content() -> None:
    file_path = os.path.join(dir_path, file_name[0])
    now: datetime = datetime.now()
    timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for i, line in enumerate(content, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args: List[str] = sys.argv[1:]
    parse_arguments(args)
    create_directories()
    if file_name:
        collect_content()
        write_content()


if __name__ == "__main__":
    main()
