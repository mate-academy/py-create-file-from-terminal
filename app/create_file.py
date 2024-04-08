import sys
import os
from datetime import datetime


def create_dir(dir_name: list[str]) -> None:
    path = os.path.join(*dir_name)
    os.makedirs(path, exist_ok=True)


def create_and_write_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        print(f"Enter content for '{file_name}' (type 'stop' to finish): ")

        line_num = 1
        while True:
            content = input(f"Enter content line {line_num}: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_num} {content}\n")
            line_num += 1


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py "
              "[-d <directory_name>] [-f <file_name>]")
        return

    if "-d" in args:
        dir_index = args.index("-d") + 1
        dir_names = args[dir_index:]
        create_dir(dir_names)

    if "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        create_and_write_file(file_name)


if __name__ == "__main__":
    main()
