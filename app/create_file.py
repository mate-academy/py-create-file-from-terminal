import sys
import os
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    """Парсить аргументи командного рядка"""
    dirs = []
    filename = None
    i = 1
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
            i += 1
    return dirs, filename


def collect_lines() -> list:
    """Збирає рядки від користувача"""
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: list) -> str:
    """Форматує контент з timestamp та нумерацією"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n"
    for i, line in enumerate(lines, 1):
        content += f"{i} {line}\n"
    return content


def write_file(file_path: str, content: str) -> None:
    """Записує контент у файл"""
    if os.path.exists(file_path):
        content = "\n" + content
    with open(file_path, "a") as file:
        file.write(content)


# Основна логіка
dirs, filename = parse_arguments(sys.argv)
if dirs:
    os.makedirs(os.path.join(*dirs), exist_ok=True)
if filename is not None:
    file_path = os.path.join(*dirs, filename) if dirs else filename
    lines = collect_lines()
    content = format_content(lines)
    write_file(file_path, content)
