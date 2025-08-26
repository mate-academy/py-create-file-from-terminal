import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    # Перевіряємо чи є аргументи
    if not args:
        print("Usage: python create_file.py -d [dir1 dir2 ...] -f filename")
        return

    # Змінні для директорій і файлу
    dirs = []
    filename = None

    # Парсимо аргументи
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: file name not provided after -f")
                return
        else:
            print(f"Unknown argument: {args[i]}")
            return

    # Якщо є директорії – створюємо їх
    path = os.getcwd()
    if dirs:
        path = os.path.join(path, *dirs)
        os.makedirs(path, exist_ok=True)

    # Якщо немає файлу – просто створюємо директорію
    if not filename:
        print(f"Directory created at: {path}")
        return

    # Повний шлях до файлу
    file_path = os.path.join(path, filename)

    # Збираємо контент
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    if not lines:
        print("No content provided. File not created/updated.")
        return

    # Запис у файл
    with open(file_path, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            f.write(f"{idx} {line}\n")

    print(f"File saved at: {file_path}")


if __name__ == "__main__":
    main()
