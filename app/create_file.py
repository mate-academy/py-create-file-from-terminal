import os
import sys
from datetime import datetime


def create_directories(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def write_file_with_content(file_path: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    if not lines:
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(timestamp + "\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")
        f.write("\n")


def main() -> None:
    args = sys.argv[1:]
    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        next_flag_index = min(
            [i for i, x in enumerate(args[d_index + 1:], start=d_index + 1)
             if x.startswith("-")]
            + [len(args)]
        )
        directories = args[d_index + 1:next_flag_index]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    path = create_directories(directories) if directories else os.getcwd()

    if file_name:
        file_path = os.path.join(path, file_name)
        write_file_with_content(file_path)


if __name__ == "__main__":
    main()
