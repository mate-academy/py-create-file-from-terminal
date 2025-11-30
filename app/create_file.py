import os
import sys
from datetime import datetime
from typing import Any


def patse_args(args: list[str]) -> tuple[bool, bool, list[Any], str | None]:
    d_flag = False
    f_flag = False
    dirs = []
    filename = None

    i = 1
    while i < len(args):
        if args[i] == "-d":
            d_flag = True
            i = i + 1
            while i < len(args) and args[i] != "-f":
                dirs.append(args[i])
                i = i + 1
        elif args[i] == "-f":
            f_flag = True
            i = i + 1
            if i < len(args):
                filename = args[i]
                i = i + 1
        else:
            i = i + 1
    return d_flag, f_flag, dirs, filename


def ask_for_content() -> list[Any]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def format_entry(lines: list[Any]) -> str:
    timestamp = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    numbered = [f"{i + 1} {line}" for i, line in enumerate(lines)]
    return timestamp + "\n" + "\n".join(numbered) + "\n"


def main() -> str | None:
    if len(sys.argv) < 2:
        print("Uzycie:")
        print("python create_file.py -d dir1 dir2 -f file.txt")
        print("python create_file.py -f file.txt")
        print("python create_file.py -d dir1 dir2")
        sys.exit(1)
    d_flag, f_flag, dirs, filename = patse_args(sys.argv)
    path = "."
    if d_flag:
        if not dirs:
            print("Podano -d, ale nie podano katalogów!")
            sys.exit(1)
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)

    if f_flag:
        if not filename:
            print("Podano -f, ale nie podano nazwy pliku!")
            sys.exit(1)
        filepath = os.path.join(path, filename)
    else:
        filename = input("Podaj nazwę pliku: ")
        filepath = os.path.join(path, filename)
    lines = ask_for_content()
    entry = format_entry(lines)
    mode = "a" if os.path.exists(filepath) else "w"
    with open(filepath, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(entry)
    print(f"\nZapisano do pliku: {filepath}")


if __name__ == "__main__":
    main()
