import sys
import os
from datetime import datetime

args = sys.argv[1:]

directory = None
filename = None
is_directory = False
is_file = False

if "-d" in args:
    d_index = args.index("-d")
    directory = args[d_index + 1]
    is_directory = True

if "-f" in args:
    f_index = args.index("-f")
    filename = args[f_index + 1]
    is_file = True

if is_directory:
    dir_path = os.path.join(directory)
    os.makedirs(dir_path, exist_ok=True)


def get_file_content() -> None:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


if is_file:
    if not is_directory:
        dir_path = ""

    content = get_file_content()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines_with_numbers = [f"{i + 1} {line}" for i, line in enumerate(content)]

    full_path = os.path.join(dir_path, filename)

    with open(full_path, "a") as f:
        if os.path.getsize(full_path) > 0:
            f.write("\n")
        f.write(f"{timestamp}\n")
        f.write("\n".join(lines_with_numbers) + "\n")

    if not is_directory and not is_file:
        print("Please provide at least one flag (-d or -f).")
