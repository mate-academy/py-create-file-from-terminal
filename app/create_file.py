import os
import sys
from datetime import datetime


def build_path(parts: list) -> str:
    if not parts:
        return os.getcwd()
    return os.path.join(os.getcwd(), *parts)


def main() -> None:
    args = sys.argv[1:]
    d_idx = args.index("-d") if "-d" in args else None
    f_idx = args.index("-f") if "-f" in args else None

    dir_parts = []
    filename = None

    if d_idx is not None:
        if f_idx is not None and d_idx < f_idx:
            dir_parts = args[d_idx + 1:f_idx]
        else:
            dir_parts = args[d_idx + 1:]
        dir_parts = [p for p in dir_parts if not p.startswith("-")]

    if f_idx is not None:
        if f_idx + 1 < len(args) and not args[f_idx + 1].startswith("-"):
            filename = args[f_idx + 1]
        else:
            print("Error: missing filename after -f")
            return

    target_dir = create_dir(dir_parts) if dir_parts else os.getcwd()

    if not filename:
        return
    target_file = os.path.join(target_dir, filename)

    create_file(target_file)


def create_dir(dir_parts: list) -> str:
    target = build_path(dir_parts)
    os.makedirs(target, exist_ok=True)
    return target


def create_file(file_path: str) -> None:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as output_file:
        output_file.write(timestamp + "\n")

        for line_number, text in enumerate(lines, start=1):
            output_file.write(f"{line_number} {text}\n")
        output_file.write("\n")


if __name__ == "__main__":
    main()
