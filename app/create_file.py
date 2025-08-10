import os
import sys
from datetime import datetime
from typing import List


def create_directory(path_parts: List[str]) -> str:
    directory = os.path.join(*path_parts)
    print(f"Attempting to create directory: {directory}")
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Директорію \'{directory}\' створено успішно.")
    else:
        print(f"Директорія \'{directory}\' вже існує.")
    return directory


def create_or_append_file(filepath: str) -> None:
    is_new_file = not os.path.exists(filepath)

    with open(filepath, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1

    if is_new_file:
        print(f"Файл \'{filepath}\' створено успішно.")
    else:
        print(f"Вміст додано до файлу \'{filepath}\'.")


def main() -> None:
    args = sys.argv[1:]
    print(f"Arguments received: {args}")

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        path_parts = args[d_index + 1:f_index]
        filename = args[f_index + 1]

        directory = create_directory(path_parts)
        filepath = os.path.join(directory, filename)
        create_or_append_file(filepath)

    elif "-d" in args:
        d_index = args.index("-d")
        path_parts = args[d_index + 1:]
        create_directory(path_parts)

    elif "-f" in args:
        f_index = args.index("-f")
        filename = args[f_index + 1]
        filepath = os.path.join(os.getcwd(), filename)
        create_or_append_file(filepath)

    else:
        print("Помилка: Потрібно вказати або -d, або -f прапори.")


if __name__ == "__main__":
    main()
