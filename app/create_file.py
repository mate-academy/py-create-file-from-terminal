import argparse
import os
from datetime import datetime


def create_folder(dirs: list[str]) -> str:
    if not dirs:
        return ""

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str, path: str = "") -> None:
    if not file_name:
        return

    file_name = os.path.join(path, file_name)
    open_mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, open_mode) as file:
        if open_mode == "a":
            file.write("\n")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")

        line_count = 0
        while True:
            line_count += 1
            line_input = input("Enter content line: ")
            if line_input == "stop":
                break
            file.write(f"{line_count} {line_input}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", action="extend", nargs="+", type=str)
    parser.add_argument("-f", "--file", action="store", type=str)
    args = parser.parse_args()
    create_file(args.file, create_folder(args.dir))


if __name__ == "__main__":
    main()
