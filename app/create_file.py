import sys
import os
import datetime


def parse_args(args: list[str]) -> tuple[str, str]:
    """Розбирає аргументи командного рядка та повертає параметри."""
    path = os.getcwd()
    file_name = ""
    index = 1

    while index < len(args):
        if args[index] == "-f" and index + 1 < len(args):
            file_name = args[index + 1]
            index += 2
            continue
        elif args[index] == "-d" and index + 1 < len(args):
            index += 1
            while index < len(args) and args[index] != "-f":
                path = os.path.join(path, args[index])
                index += 1
            continue
        index += 1

    return path, file_name


def append_interactive_content(file_path: str) -> None:
    """Записує поточний час та введені користувачем рядки у файл."""
    with open(file_path, "a") as file:

        if file.tell() != 0:
            file.write("\n")

        format_time = "%Y-%m-%d %H:%M:%S"
        file.write(datetime.datetime.now().strftime(format_time) + "\n")

        line_count = 1
        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            file.write(f"{line_count} {line}\n")
            line_count += 1


path, file_name = parse_args(sys.argv)

# 1. Створюємо директорію, якщо не поточна
if path != os.getcwd():
    os.makedirs(path)

# 2. Записуємо у файл якщо ім'я файлу не порожнє
if file_name:
    file_path = os.path.join(path, file_name)
    append_interactive_content(file_path)
