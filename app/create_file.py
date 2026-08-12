import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d <dirs...> -f <filename>")
        return

    dir_path = None
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []
        for i in range(d_index + 1, len(args)):
            if args[i].startswith("-"):
                break
            dir_parts.append(args[i])
        if dir_parts:
            dir_path = os.path.join(*dir_parts)
            os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if not file_name:
        if dir_path:
            print(f"Directory created: {dir_path}")
        else:
            print("No file or directory specified.")
        return

    if dir_path:
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {line}" for i, line in enumerate(lines)]
    block = "\n".join([timestamp] + numbered_lines)

    with open(file_path, "a", encoding="utf-8") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write(block)

    print(f"File created/updated: {file_path}")


if __name__ == "__main__":
    main()
