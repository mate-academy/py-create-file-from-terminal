import sys
import os
from datetime import datetime
from typing import List


def extract_directories(args: List[str]) -> List[str]:
    """Извлекает части пути после флага -d и до -f."""
    if "-d" not in args:
        return []

    directories = []
    start_index = args.index("-d") + 1

    for arg in args[start_index:]:
        if arg == "-f":
            break
        directories.append(arg)

    return directories


def extract_filename(args: List[str]) -> str | None:
    """Извлекает имя файла после флага -f."""
    if "-f" not in args:
        return None

    index_file = args.index("-f") + 1

    if index_file >= len(args):
        return None

    return args[index_file]


def collect_content() -> List[str]:
    """Собирает строки контента от пользователя, пока он не введёт stop."""
    lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    return lines


def write_content(path: str, lines: List[str]) -> None:
    """Записывает контент в файл с датой и нумерацией."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a" if os.path.exists(path) else "w"

    with open(path, mode, encoding="utf-8") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")
        file.write("\n")  # пустая строка между блоками


def main() -> None:
    args = sys.argv[1:]

    directories = extract_directories(args)
    file_name = extract_filename(args)

    # Создаём каталоги, если они указаны
    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directories created at: {directory_path}")

    # Если файла нет — программа завершает работу
    if file_name is None:
        return

    # Определяем путь к файлу
    if directories:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    # Сбор контента и запись
    content_lines = collect_content()
    write_content(file_path, content_lines)
    print(f"File created/updated at: {file_path}")


if __name__ == "__main__":
    main()
