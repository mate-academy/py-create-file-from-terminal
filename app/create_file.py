import os
import sys
from datetime import datetime
from typing import Any


CURRENT_TIMESTAMP_STR = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def make_directory(directory_path: str | bytes) -> Any:
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(file_name: str) -> None:
    with open(file_name, "a") as new_file:
        line_number = 1
        new_file.write(f"{CURRENT_TIMESTAMP_STR}\n")
        while True:
            user_input = input("Введіть вміст "
                               "рядка (або 'stop' для завершення): ")
            if user_input.lower() == "stop":
                break
            new_file.write(f"{line_number} {user_input}\n")
            line_number += 1
        new_file.write("\n")


def main() -> None:
    args = sys.argv[1:]

    directory_path = None
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            if i + 1 < len(args) and not args[i + 1].startswith("-"):
                directory_path = args[i + 1]
                i += 2
            else:
                print("Помилка: Після прапорця '-d' "
                      "відсутній шлях до директорії.", file=sys.stderr)
                sys.exit(1)
        elif args[i] == "-f":
            if i + 1 < len(args) and not args[i + 1].startswith("-"):
                file_name = args[i + 1]
                i += 2
            else:
                print("Помилка: Після "
                      "прапорця '-f' відсутнє ім'я файлу.", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Помилка: Невідомий аргумент '{args[i]}'.", file=sys.stderr)
            sys.exit(1)

    if directory_path and file_name:
        full_dir_path = make_directory(directory_path)
        file_full_path = os.path.join(full_dir_path, file_name)
        create_file(file_full_path)
        print(f"Директорія '{full_dir_path}' "
              f"створена та файл '{file_name}' створений у ній.")
    elif directory_path:
        make_directory(directory_path)
        print(f"Директорія '{directory_path}' успішно створена.")
    elif file_name:
        create_file(file_name)
        print(f"Файл '{file_name}' успішно створений у поточній директорії.")
    else:
        print("Використання: script.py [-d "
              "<шлях_до_директорії>] [-f <ім'я_файлу>]", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
