import sys
import os
from datetime import datetime

def parse_arguments(args):
    """
    Парсинг аргументів командного рядка:
    -d <directories> - список директорій
    -f <file_name> - назва файлу
    """
    directories = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # збираємо всі аргументи до наступного прапорця або кінця
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i >= len(args):
                print("Помилка: після -f не вказано назву файлу.")
                sys.exit(1)
            file_name = args[i]
            i += 1
        else:
            i += 1
    return directories, file_name

def main():
    args = sys.argv[1:]
    directories, file_name = parse_arguments(args)

    # Створюємо шлях до директорій
    dir_path = ""
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    if not file_name:
        print("Помилка: не вказано файл для запису.")
        sys.exit(1)

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    # Зчитуємо рядки контенту від користувача
    content_lines = []
    print("Вводьте рядки контенту. Напишіть 'stop', щоб завершити.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "stop":
            break
        content_lines.append(user_input)

    if not content_lines:
        print("Немає рядків для запису.")
        sys.exit(0)

    # Формуємо текст для запису з timestamp і нумерацією рядків
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_lines = [timestamp]
    for index, line in enumerate(content_lines, start=1):
        output_lines.append(f"{index} {line}")
    output_lines.append("")  # пустий рядок після всього контенту

    with open(file_path, "a", encoding="utf-8") as file_obj:
        file_obj.write("\n".join(output_lines) + "\n")

    print(f"Контент успішно записано у файл: {file_path}")

if __name__ == "__main__":
    main()