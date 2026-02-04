import sys
import os
from datetime import datetime


def red_content_file() -> None:
    lines = []
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{line} {counter}")
        counter += 1

    return lines


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print(" python create_file.py -d dir1 dir2 ...")
        print(" python create_file.py -f filename")
        print(" python create_file.py -d dir1 dir2 -f filename")
        return

    dir_parts = []
    filename = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue

        i += 1

    dir_path = ""
    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if dir_parts and filename is None:
        print(f"Directory created: {dir_path}")
        return

    if filename:
        if dir_path:
            full_path = os.path.join(dir_path, filename)
        else:
            filename

        print(f"Creating file: {full_path}")

        content_lines = red_content_file()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        write_mode = "a" if os.path.exists(full_path) else "w"

        with open(full_path, write_mode, encoding="utf-8") as f:
            if write_mode == "a":
                f.write("\n")
            f.write(timestamp + "\n")
            for line in content_lines:
                f.write(line + "\n")

        print(f"File saved: {full_path}")


if __name__ == "__main__":
    main()
