import sys
import os
from datetime import datetime


def create_dir(path_parts: str) -> None:
    os.makedirs("/".join(path_parts), exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n")
        now = datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        user_input = input("Enter content line: ")
        while user_input != "stop":
            f.write(f"{count} {user_input}\n")
            count += 1
            user_input = input("Enter content line: ")


def main() -> None:
    args = sys.argv
    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        dir_parts = args[d_index + 1:f_index]
        file_name = args[f_index + 1]

        # Создаем директорию
        if dir_parts:
            create_dir(dir_parts)

        # Создаем файл внутри директории
        file_path = "/".join(dir_parts + [file_name])
        create_file(file_path)

    elif "-d" in args:
        d_index = args.index("-d")
        dir_parts = args[d_index + 1:]
        create_dir(dir_parts)

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)


if __name__ == "__main__":
    main()
