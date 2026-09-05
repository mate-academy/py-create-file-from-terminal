import sys
import os
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments(arg: List[str]) -> Tuple[List[str], Optional[str]]:
    """
    Analizuje listę argumentów i zwraca:
    - directories: lista segmentów ścieżki katalogu (może być pusta)
    - filename: nazwa pliku (lub None, jeśli nie podano -f)
    Działa niezależnie od kolejności flag -d i -f.
    """
    d_idx = arg.index("-d") if "-d" in arg else None
    f_idx = arg.index("-f") if "-f" in arg else None

    directories: List[str] = []
    if d_idx is not None:
        if f_idx is not None and f_idx > d_idx:
            directories = arg[d_idx + 1: f_idx]
        else:
            directories = arg[d_idx + 1:]

    filename: Optional[str] = None
    if f_idx is not None:
        filename = arg[f_idx + 1]

    return directories, filename


def create_directories(directories: List[str]) -> str:
    """
    Buduje ścieżkę katalogu z listy segmentów i tworzy ją na dysku.
    Zwraca zbudowaną ścieżkę (pusty string, jeśli lista jest pusta).
    """
    path = ""
    for elem in directories:
        path = os.path.join(path, elem)

    if path:
        os.makedirs(path, exist_ok=True)

    return path


def collect_content_lines() -> List[str]:
    """
    Pyta użytkownika o kolejne linie treści, aż wpisze "stop".
    Zwraca listę wpisanych linii (bez słowa "stop").
    """
    lines: List[str] = []
    while True:
        inp = input("Enter content line: ")
        if inp == "stop":
            break
        lines.append(inp)
    return lines


def write_content_to_file(file_path: str, lines: List[str]) -> None:
    """
    Zapisuje znacznik czasu i ponumerowane linie treści do pliku.
    Jeśli plik już istnieje, dopisuje pustą linię jako separator
    przed nowym wpisem. Timestamp jest liczony w momencie zapisu,
    a nie przy starcie programu.
    """
    current_time = datetime.now()
    formated_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as new_file:
        if file_exists:
            new_file.write("\n")
        new_file.write(formated_time + "\n")
        for line_num, line in enumerate(lines, start=1):
            new_file.write(f"{line_num} {line}\n")


def main() -> None:
    arg = sys.argv[1:]

    directories, filename = parse_arguments(arg)
    directory_path = create_directories(directories)

    if filename is not None:
        file_path = os.path.join(directory_path, filename)
        lines = collect_content_lines()
        write_content_to_file(file_path, lines)


main()
