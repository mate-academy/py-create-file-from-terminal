import sys
import os
from datetime import datetime


# Розбір аргументів з терміналу
def parse_args(args: list) -> tuple:
    path_parts = []
    file_name = None
    i = 1
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                path_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1
    return path_parts, file_name


# Отримання рядків вмісту з терміналу
def get_content_lines() -> list:
    lines = []
    while True:
        line = input("Введіть рядок вмісту: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


# Запис у файл з датою та нумерацією
def write_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv
    if len(args) < 2:
        print("Вкажіть хоча б один аргумент -d або -f.")
        return

    path_parts, file_name = parse_args(args)

    # Створення директорії, якщо задано
    dir_path = os.path.join(*path_parts) if path_parts else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    # Перевірка, чи задано файл
    if file_name:
        full_file_path = os.path.join(dir_path, file_name) if (
            dir_path) else file_name
        content_lines = get_content_lines()
        write_to_file(full_file_path, content_lines)
        print(f"Файл створено або оновлено: {full_file_path}")
    else:
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Директорію створено: {dir_path}")


if __name__ == "__main__":
    main()
