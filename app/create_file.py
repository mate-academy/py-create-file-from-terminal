import os
import sys
from datetime import datetime
from typing import List, Tuple, Optional


def parse_args(args: List[str]) -> Tuple[bool, bool, List[str], Optional[str]]:
    d_flag = False
    f_flag = False
    dirs: List[str] = []
    filename: Optional[str] = None

    i = 1
    while i < len(args):
        if args[i] == "-d":
            d_flag = True
            i += 1
            while i < len(args) and args[i] != "-f":
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            f_flag = True
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    return d_flag, f_flag, dirs, filename


def ask_for_content() -> List[str]:
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def format_entry(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered = [f"{i + 1} {line}" for i, line in enumerate(lines)]
    return timestamp + "\n" + "\n".join(numbered) + "\n"


def main() -> None:
    if len(sys.argv) < 2:
        print("Użycie:")
        print("python create_file.py -d dir1 dir2")
        print("python create_file.py -f file.txt")
        print("python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    d_flag, f_flag, dirs, filename = parse_args(sys.argv)

    path = "."
    if d_flag:
        if not dirs:
            print("Podano -d bez katalogów.")
            sys.exit(1)
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
        print(f"Utworzono katalog(i): {path}")
        if not f_flag:
            print("Nie podano -f — kończę działanie.")
            sys.exit(0)

    if f_flag:
        if not filename:
            print("Podano -f bez nazwy pliku.")
            sys.exit(1)
        file_path = os.path.join(path, filename)
    else:
        print("Nie podano flagi -f.")
        sys.exit(1)

    lines = ask_for_content()
    if not lines:
        print("Brak danych — nic nie zapisano.")
        sys.exit(0)

    entry = format_entry(lines)
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n")
        f.write(entry)

    print(f"Zapisano do pliku: {file_path}")


if __name__ == "__main__":
    main()
