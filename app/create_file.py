import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2 ...")
        print("  python create_file.py -f filename")
        print("  python create_file.py -d dir1 dir2 ... -f filename")
        return

    dirs = []
    filename = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            continue
        elif args[i] == "-f":
            if i + 1 < len(args):
                filename = args[i + 1]
                i += 2
                continue
            else:
                print("Error: -f flag requires a filename")
                return
        else:
            print(f"Unknown argument: {args[i]}")
            return

    base_path = os.getcwd()
    if dirs:
        dir_path = os.path.join(base_path, *dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = base_path

    if filename:
        file_path = os.path.join(dir_path, filename)

        lines = []
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            lines.append(line)

        if lines:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"\n{timestamp}\n")
                for i, line in enumerate(lines, 1):
                    f.write(f"{i} {line}\n")

        print(f"File created/updated: {file_path}")
    else:
        if dirs:
            print(f"Directory created: {dir_path}")


if __name__ == "__main__":
    main()
