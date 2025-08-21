# write your code here
import sys
import os
from datetime import datetime


def create_directory(path_parts):
    """Створює директорію з частин шляху."""
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_file_content():
    """Отримує вміст файлу від користувача."""
    lines = []
    print("Enter content lines (type 'stop' to finish):")

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def format_content(lines):
    """Форматує вміст файлу з номерами рядків та часовою позначкою."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [timestamp]

    for i, line in enumerate(lines, 1):
        formatted_lines.append(f"{i} {line}")

    return "\n".join(formatted_lines)


def create_file_with_content(file_path, content):
    """Створює файл з вмістом або додає до існуючого."""
    # Перевіряємо чи файл існує
    if os.path.exists(file_path):
        # Додаємо до існуючого файлу
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n\n" + content)
    else:
        # Створюємо новий файл
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)


def parse_arguments(args):
    """Парсить аргументи командного рядка."""
    directory_parts = []
    file_name = None

    i = 1  # Пропускаємо назву скрипта
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # Збираємо всі частини директорії до наступного флага або кінця
            while i < len(args) and not args[i].startswith("-"):
                directory_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return directory_parts, file_name


def main():
    """Головна функція програми."""
    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    directory_parts, file_name = parse_arguments(sys.argv)

    # Визначаємо шлях до файлу
    if directory_parts and file_name:
        # Обидва флаги: створюємо директорію та файл всередині
        directory_path = create_directory(directory_parts)
        file_path = os.path.join(directory_path, file_name)

        # Отримуємо вміст та створюємо файл
        content_lines = get_file_content()
        formatted_content = format_content(content_lines)
        create_file_with_content(file_path, formatted_content)

        print(f"Directory '{directory_path}' created.")
        print(f"File '{file_path}' created with content.")

    elif directory_parts:
        # Тільки -d флаг: створюємо директорію
        directory_path = create_directory(directory_parts)
        print(f"Directory '{directory_path}' created.")

    elif file_name:
        # Тільки -f флаг: створюємо файл в поточній директорії
        content_lines = get_file_content()
        formatted_content = format_content(content_lines)
        create_file_with_content(file_name, formatted_content)

        print(f"File '{file_name}' created with content.")

    else:
        print("Error: No valid flags provided.")
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")


if __name__ == "__main__":
    main()