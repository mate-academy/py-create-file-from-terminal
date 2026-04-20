import sys
import os
from datetime import datetime
from typing import List, Optional


def main() -> None:
    args: List[str] = sys.argv[1:]

    if not args:
        print(
            "Usage: python create_file.py "
            "[-d dir1 dir2 ...] [-f filename]"
        )
        sys.exit(1)

    dir_parts: List[str] = []
    filename: Optional[str] = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: -f flag requires a filename")
                sys.exit(1)
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    # --- Tworzenie katalogów ---
    target_dir = os.path.join(*dir_parts) if dir_parts else "."
    os.makedirs(target_dir, exist_ok=True)

    # --- Tylko katalog, bez pliku ---
    if filename is None:
        abs_dir = os.path.abspath(target_dir)
        print(f"Directory created: {abs_dir}")
        return

    # --- Tworzenie pliku z zawartością ---
    filepath = os.path.join(target_dir, filename)

    print("Enter content line (type 'stop' to finish):")
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        # Dokładne, case-sensitive dopasowanie bez strip/lower
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(filepath)

    with open(filepath, "a", encoding="utf-8") as file_handle:
        # Pusta linia tylko jeśli plik już istniał (nowy blok)
        if file_exists:
            file_handle.write("\n")

        file_handle.write(f"{timestamp}\n")
        for idx, content_line in enumerate(lines, start=1):
            file_handle.write(f"{idx} {content_line}\n")

    print(f"File created/updated: {os.path.abspath(filepath)}")


if __name__ == "__main__":
    main()
