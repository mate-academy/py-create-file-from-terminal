import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_content(file_path: str) -> None:
    print("\nEnter content line (type 'stop' to finish):")
    lines: list[str] = []

    while True:
        line: str = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(get_timestamp() + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")
        f.write("\n")


def main() -> None:
    args: list[str] = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_path: list[str] = []
    file_name: str | None = None

    if "-d" in args:
        d_index: int = args.index("-d")
        next_flag: int = len(args)
        if "-f" in args:
            next_flag = args.index("-f")
        dir_path = args[d_index + 1:next_flag]

    if "-f" in args:
        f_index: int = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    final_dir: str = os.path.join(os.getcwd(),
                                  *dir_path) if dir_path else os.getcwd()

    if dir_path:
        os.makedirs(final_dir, exist_ok=True)
        print(f"Created directory: {final_dir}")

    if file_name:
        file_path: str = os.path.join(final_dir, file_name)
        print(f"Writing to file: {file_path}")
        write_content(file_path)
        print("File updated.")


if __name__ == "__main__":
    main()
