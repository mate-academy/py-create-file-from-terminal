import sys
import os
from datetime import datetime


def parse_args(
        args: list[str]
) -> tuple[list[str], str | None]:
    """Разбирает аргументы командной строки,
    возвращает (список папок, имя файла)."""
    dirs = []
    filename = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # Собираем все имена папок, пока не встретим -f или конец
            while i < len(args) and args[i] != "-f":
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    return dirs, filename


def get_content_lines() -> list[str]:
    """Читает строки контента от пользователя до слова 'stop'."""
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file(dirs: list[str], filename: str) -> None:
    """Создаёт папки и файл с контентом."""
    # Определяем путь к директории
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    # Полный путь к файлу
    file_path = os.path.join(dir_path, filename)

    # Получаем контент от пользователя
    lines = get_content_lines()

    # Формируем блок контента: timestamp + нумерованные строки
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = [timestamp]
    for i, line in enumerate(lines, start=1):
        content_lines.append(f"{i} {line}")

    content_block = "\n".join(content_lines)

    # Если файл уже существует — добавляем пустую строку перед новым блоком
    if os.path.exists(file_path):
        content_block = "\n" + content_block

    # Записываем в файл (режим "a" — дозапись)
    with open(file_path, "a") as f:
        f.write(content_block + "\n")


def main() -> None:
    args = sys.argv[1:]
    dirs, filename = parse_args(args)

    if not dirs and not filename:
        print("No arguments provided. "
              "Use -d for directories and/or -f for file.")
        return

    if dirs and not filename:
        # Только папки — создаём и выходим
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    elif filename:
        # Есть файл — создаём (с папками, если указаны)
        create_file(dirs, filename)


main()
