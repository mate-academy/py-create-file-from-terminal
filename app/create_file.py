import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f filename")
        print("  python create_file.py -d dir1 dir2 -f filename")
        return

    dir_parts = []
    file_name = None

    # parse flags
    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []
        for i in range(d_index + 1, len(args)):
            if args[i].startswith("-"):
                break
            dir_parts.append(args[i])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Error: you must provide a file name after -f")
            return

    target_dir = (
        os.path.join(os.getcwd(), *dir_parts)
        if dir_parts else os.getcwd()
    )

    # create directories if needed
    if dir_parts:
        os.makedirs(target_dir, exist_ok=True)
        print(f"Directory created: {target_dir}")

    # if no file name, only directory creation, then exit
    if not file_name:
        return

    file_path = os.path.join(target_dir, file_name)

    print("Enter content lines. Type 'stop' to finish.")
    content_lines = []
    line_num = 1
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(f"{line_num} {line}")
        line_num += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(file_path, "a") as f:
            f.write(f"{timestamp}\n")
            for line in content_lines:
                f.write(f"{line}\n")
            f.write("\n")
        print(f"File updated: {file_path}")
    except Exception as e:
        print(f"Error writing file: {e}")


if __name__ == "__main__":
    main()
