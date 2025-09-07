import sys
from datetime import datetime
import os


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    """Парсимо аргументи -d і -f."""
    directory_parts: list[str] = []
    filename: str | None = None
    index = 0

    while index < len(arguments):
        token = arguments[index]
        if token == "-d":
            index += 1
            while (index < len(arguments)
                   and not arguments[index].startswith("-")):
                directory_parts.append(arguments[index])
                index += 1
            continue
        if token == "-f":
            index += 1
            if index >= len(arguments) or arguments[index].startswith("-"):
                raise ValueError("Error: -f flag requires a file name.")
            filename = arguments[index]
        else:
            raise ValueError(f"Error: unknown argument '{token}'.")
        index += 1

    return directory_parts, filename


def ensure_directories(directory_parts: list[str]) -> str:
    """Створює директорії і повертає шлях"""
    if not directory_parts:
        return "."
    target_dir = os.path.join(*directory_parts)
    os.makedirs(target_dir, exist_ok=True)
    return target_dir


def collect_content() -> list[str]:
    """Збирає рядки до введення 'stop'."""
    content: list[str] = []
    while True:
        try:
            line = input("Enter content line: ")
        except EOFError:
            break
        if line == "stop":
            break
        content.append(line)
    return content


def append_block(file_path: str, content: list[str]) -> None:
    """Додає вказаний контент у файл із таймштампом та нумерацією."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered = [f"{i} {line}" for i, line
                in enumerate(content, start=1)]
    prepend_blank = (os.path.exists(file_path)
                     and os.path.getsize(file_path) > 0)

    with open(file_path, "a", encoding="utf-8") as file_obj:
        if prepend_blank:
            file_obj.write("\n")
        file_obj.write(f"{timestamp}\n")
        for row in numbered:
            file_obj.write(row + "\n")


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    try:
        directory_parts, file_name = parse_arguments(sys.argv[1:])
    except ValueError as error:
        print(error, file=sys.stderr)
        sys.exit(1)

    base_dir = ensure_directories(directory_parts)

    if file_name is None:
        print(f"Created directory: {os.path.abspath(base_dir)}")
        return

    content_lines = collect_content()
    file_path = os.path.join(base_dir, file_name)
    append_block(file_path, content_lines)
    print(f"Wrote {len(content_lines)} lines to: {os.path.abspath(file_path)}")


if __name__ == "__main__":
    main()
