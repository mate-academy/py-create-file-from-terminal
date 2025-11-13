"""Utility for creating directories and writing content to files."""

import os
from datetime import datetime
from pathlib import Path


def create_directories(path_parts):
    """
    Create nested directories based on the given path parts.

    Args:
        path_parts (list[str]): List of path parts to join.

    Returns:
        Path: Path object representing the created directory.
    """
    dir_path = Path(path_parts[0])
    for part in path_parts[1:]:
        dir_path = dir_path / part

    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def write_to_file(file_path, lines):
    """
    Write lines to a file with timestamp and line numbering.

    Args:
        file_path (str | Path): Path to the file to write.
        lines (list[str]): Lines to write.
    """
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"Created: {timestamp}\n\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i}. {line}\n")


def get_content_from_user():
    """
    Prompt user for lines of text until 'stop' is entered.

    Returns:
        list[str]: List of entered lines.
    """
    content = []
    while True:
        line = input("Введите строку (или 'stop' для завершения): ")
        if line.strip().lower() == "stop":
            break
        content.append(line)
    return content


def main():
    """Command-line entry point for creating a file."""
    print("=== Создание файла ===")
    folder_path = input("Введите путь к папке: ").strip()
    file_name = input("Введите имя файла (например example.txt): ").strip()

    lines = get_content_from_user()

    dir_path = create_directories([folder_path])
    file_path = Path(dir_path) / file_name

    write_to_file(file_path, lines)
    print(f"\nФайл успешно создан: {file_path.absolute()}")


if __name__ == "__main__":
    main()
