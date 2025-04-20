import sys
import os
from datetime import datetime


def parse_args(argv: list[str]) -> tuple[list[str], str | None]:
    """Парсинг аргументів командного рядка."""
    dir_parts = []
    file_name = None

    if "-d" in argv:
        d_index = argv.index("-d")
        if "-f" in argv:
            f_index = argv.index("-f")
            dir_parts = argv[d_index + 1:f_index]
        else:
            dir_parts = argv[d_index + 1:]
    if "-f" in argv:
        f_index = argv.index("-f")
        file_name = argv[f_index + 1] if f_index + 1 < len(argv) else None

    return dir_parts, file_name


def prompt_for_content() -> list[str]:
    """Запитує рядки контенту до 'stop'."""
    print("\nВведіть вміст рядків. Для завершення введіть 'stop'")
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    """Записує вміст до файлу з таймштампом та нумерацією."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    dir_parts, file_name = parse_args(sys.argv)

    # Якщо тільки директорія - створюємо її
    if dir_parts and not file_name:
        dir_path = os.path.join(os.getcwd(), *dir_parts)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Створено директорію: {dir_path}")
        return

    # Якщо тільки файл
    if not dir_parts and file_name:
        file_path = os.path.join(os.getcwd(), file_name)
        content_lines = prompt_for_content()
        write_to_file(file_path, content_lines)
        print(f"Вміст додано до файлу: {file_path}")
        return

    # Якщо і директорія, і файл
    if dir_parts and file_name:
        dir_path = os.path.join(os.getcwd(), *dir_parts)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, file_name)
        content_lines = prompt_for_content()
        write_to_file(file_path, content_lines)
        print(f"Файл створено: {file_path}")
        return

    # Якщо нічого не передано
    print("Помилка: передайте флаг -d або -f або обидва.")
    print("Приклад використання:")
    print("  python create_file.py -d dir1 dir2")
    print("  python create_file.py -f file.txt")
    print("  python create_file.py -d dir1 dir2 -f file.txt")


if __name__ == "__main__":
    main()
