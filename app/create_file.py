import os
import sys
from datetime import datetime


def read_lines() -> list[str]:
    lines = []
    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        lines.append(text)
    return [f"{i + 1} {line}" for i, line in enumerate(lines)]


def write_to_file(path: str, filename: str, lines: list[str]) -> None:
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, filename)
    with open(full_path, "a", encoding="utf-8") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in lines:
            f.write(line + "\n")
        f.write("\n")


def main() -> None:
    args = sys.argv[1:]
    path = os.getcwd()
    filename = None

    if "-d" in args:
        idx = args.index("-d")
        end = args.index("-f") if "-f" in args else len(args)
        dirs = args[idx + 1:end]
        if dirs:
            path = os.path.join(path, *dirs)

    if "-f" in args:
        idx = args.index("-f")
        if idx + 1 < len(args):
            filename = args[idx + 1]

    if not filename:
        print("Musisz podać nazwę pliku za pomocą -f")
        sys.exit(1)

    lines = read_lines()
    write_to_file(path, filename, lines)


if __name__ == "__main__":
    main()
