import sys
import os
import datetime


def write_content_to_file(file_path: str) -> None:
    is_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a") as file:
        if is_not_empty:
            file.write("\n")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")
        input_line_number = 1
        while (input_line := input("Enter content line: ")) != "stop":
            file.write(f"{input_line_number} {input_line}\n")
            input_line_number += 1


has_d = "-d" in sys.argv
has_f = "-f" in sys.argv

if has_d and has_f:
    d_idx = sys.argv.index("-d")
    f_idx = sys.argv.index("-f")

    if d_idx < f_idx:
        folders = sys.argv[d_idx + 1:f_idx]
        file_name = sys.argv[f_idx + 1] if f_idx + 1 < len(sys.argv) else None
    else:
        file_name = sys.argv[f_idx + 1] if f_idx + 1 < len(sys.argv) else None
        folders = sys.argv[d_idx + 1:]

    if folders and file_name is not None:
        folders_path = os.path.join(*folders)
        os.makedirs(folders_path, exist_ok=True)
        file_path = os.path.join(folders_path, file_name)
        write_content_to_file(file_path)

elif has_d:
    d_idx = sys.argv.index("-d")
    folders = sys.argv[d_idx + 1:]
    if folders:
        folders_path = os.path.join(*folders)
        os.makedirs(folders_path, exist_ok=True)

elif has_f:
    f_idx = sys.argv.index("-f")
    file_name = sys.argv[f_idx + 1] if f_idx + 1 < len(sys.argv) else None

    if file_name is not None:
        write_content_to_file(file_name)
