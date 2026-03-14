import os
import sys
from datetime import datetime


def get_user_lines() -> list:
    lines = []
    print(
        "Enter content line (type 'stop' to finish):"
    )
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as target_file:
        if mode == "a":
            target_file.write("\n")

        target_file.write(f"{timestamp}\n")
        for line_number, content in enumerate(lines, 1):
            target_file.write(f"{line_number} {content}\n")


def main() -> None:
    args = sys.argv[1:]
    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        next_flag_index = args.index("-f") if "-f" in args else len(args)
        directory_parts = args[d_index + 1 : next_flag_index]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    target_path = os.path.join(*directory_parts) if directory_parts else "."

    if directory_parts:
        os.makedirs(target_path, exist_ok=True)

    if file_name:
        full_file_path = os.path.join(target_path, file_name)
        content_lines = get_user_lines()
        write_to_file(full_file_path, content_lines)
    else:
        print("No file specified, directory created (if applicable).")


if __name__ == "__main__":
    main()
