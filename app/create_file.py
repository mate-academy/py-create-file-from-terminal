import os
import sys
from datetime import datetime


def create_directory(args: list) -> str:
    if "-d" not in args:
        return ""

    d_index = args.index("-d")

    # Визначаємо кінець списку папок
    if "-f" in args:
        f_index = args.index("-f")
        directories = args[d_index + 1: f_index]
    else:
        directories = args[d_index + 1:]

    if directories:
        full_path = os.path.join(*directories)
        os.makedirs(full_path, exist_ok=True)
        return full_path

    return ""


def write_content_to_file(file_path: str) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.seek(0, 2)
        if file.tell() > 0:
            file.write("\n")

        file.write(f"{current_time}\n")

        page_count = 1
        while True:
            message = input("Enter content line:")
            if message == "stop":
                break
            file.write(f"{page_count} {message}\n")
            page_count += 1


def main() -> None:
    args = sys.argv

    # Крок 1: Створюємо папки (якщо треба) і отримуємо шлях
    current_dir = create_directory(args)

    # Крок 2: Працюємо з файлом (якщо треба)
    if "-f" in args:
        f_index = args.index("-f")

        if f_index + 1 >= len(args):
            print("Error: provide a filename after -f")
            sys.exit(1)

        file_name = args[f_index + 1]
        full_file_path = os.path.join(current_dir, file_name)

        write_content_to_file(full_file_path)


if __name__ == "__main__":
    main()
