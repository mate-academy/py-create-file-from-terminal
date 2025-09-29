import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def parse_args(argv: List[str]) -> Tuple[List[str], Optional[str]]:

    dir_parts: List[str] = []
    file_name: Optional[str] = None

    if "-d" in argv:
        d_idx = argv.index("-d")
        f_idx = argv.index("-f") if "-f" in argv else len(argv)
        dir_parts = argv[d_idx + 1: f_idx]

    if "-f" in argv:
        f_idx = argv.index("-f")
        d_idx = argv.index("-d") if "-d" in argv else len(argv)
        if f_idx + 1 < len(argv) and (f_idx + 1 < d_idx or "-d" not in argv):
            file_name = argv[f_idx + 1]
        elif f_idx + 1 < len(argv) and "-d" not in argv:
            file_name = argv[f_idx + 1]
        else:
            if f_idx + 1 < len(argv):
                file_name = argv[f_idx + 1]

    return dir_parts, file_name


def read_lines_until_stop() -> List[str]:
    lines: List[str] = []
    counter = 1
    while True:
        line = input("Введіть рядок вмісту: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def write_with_timestamp(path: str, lines: List[str]) -> None:
    if not lines:
        print("Вміст не введено, файл не змінено.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n" + "\n".join(lines) + "\n"

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    with open(path, "a", encoding="utf-8") as f:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            f.write("\n")
        f.write(content)

    print(f"Файл '{path}' створено/оновлено.")


def main() -> None:
    dir_parts, file_name = parse_args(sys.argv[1:])

    if not dir_parts and not file_name:
        print("Використання: python create_file.py [-d dir1 dir2 ...] [-f file.txt]")
        return

    dir_path = os.path.join(*dir_parts) if dir_parts else ""

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        full_path = os.path.join(dir_path, file_name) if dir_path else file_name
        lines = read_lines_until_stop()
        write_with_timestamp(full_path, lines)
    else:
        print(f"Каталог '{dir_path}' створено (або вже існував).")


if __name__ == "__main__":
    main()