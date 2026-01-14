import sys
import os
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    dir_list: list[str] = []
    file_name: str | None = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                dir_list.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                sys.exit(1)
        else:
            i += 1

    return dir_list, file_name


def create_directories(dir_list: list[str], file_name: str | None) -> str:
    if dir_list:
        path = os.path.join(*dir_list)
        os.makedirs(path, exist_ok=True)
    else:
        path = ""

    if file_name:
        file_path = os.path.join(path, file_name) if path else file_name
        return file_path
    else:
        return path


def write_file(file_path: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    if not lines:
        return

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(timestamp + "\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")
        file.write("\n")


if __name__ == "__main__":
    dir_list, file_name = parse_arguments()
    file_path = create_directories(dir_list, file_name)
    if file_name:
        write_file(file_path)
