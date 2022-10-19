import sys

import os

from datetime import datetime


def create_file(file_name: str, mode: str) -> None:
    date_today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, mode) as file:
        file.write(date_today + "\n")
        lines = ""
        count_lines = 0
        for line in sys.stdin:
            if "stop" == line.rstrip():
                break
            count_lines += 1
            print(f"Enter content line: {line}")
            lines += f"{count_lines} {line}"
        file.write(f"{lines}\n")


def create_directory(first_dir: str, second_dir: str) -> None:
    cwd = os.getcwd()
    path = os.path.join(cwd, "app", first_dir, second_dir)
    os.makedirs(path)


def main() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        create_directory(sys.argv[-2], sys.argv[-1])
    if "-f" in sys.argv and "-d" not in sys.argv:
        create_file(f"app/{sys.argv[-1]}", "a")
    if "-d" in sys.argv and "-f" in sys.argv:
        create_directory(sys.argv[-4], sys.argv[-3])
        create_file(f"app/dir1/dir2/{sys.argv[-1]}", "w")


if __name__ == "__main__":
    main()
