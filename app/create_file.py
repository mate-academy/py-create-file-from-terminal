import sys
import os
from datetime import datetime

args = sys.argv[1:]

directory_path_components = []
file_name = None

if "-d" in args:
    directory_flag_index = args.index("-d")
    for arg in args[directory_flag_index + 1:]:
        if arg.startswith("-"):
            break
        directory_path_components.append(arg)

if "-f" in args:
    file_flag_index = args.index("-f")
    if file_flag_index + 1 >= len(args) or args[file_flag_index + 1].startswith("-"):
        print("Error: Missing file name after -f.")
        sys.exit(1)
    file_name = args[file_flag_index + 1]

directory_path = os.path.join(*directory_path_components) if directory_path_components else ""

if directory_path:
    os.makedirs(directory_path, exist_ok=True)

if file_name:
    full_file_path = os.path.join(directory_path, file_name) if directory_path else file_name

    print("Enter content lines (type 'stop' to finish):")
    user_lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        user_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(full_file_path, "a", encoding="utf-8") as file:
            file.write(f"\n{timestamp}\n")
            for index, line in enumerate(user_lines, start=1):
                file.write(f"{index} {line}\n")
        print(f"Saved to: {full_file_path}")
    except Exception as e:
        print(f"Error: {e}")
else:
    if not directory_path:
        print("Usage: -d [dir1 dir2 ...] -f [filename]")
