import sys
import os
from datetime import datetime


# Check if flags are correct
def flags_in_arg() -> bool:
    has_any_flag = "-d" in sys.argv[1:] or "-f" in sys.argv[1:]
    both_flags = "-d" in sys.argv[1:] and "-f" in sys.argv[1:]
    flags_order_correct = both_flags and (sys.argv.index("-d") < sys.argv.index("-f"))
    has_no_duplicates = sys.argv.count("-d") <= 1 and sys.argv.count("-f") <= 1
    return (
        has_any_flag and (not both_flags or flags_order_correct) and has_no_duplicates
    )


f_index = sys.argv.index("-f") if "-f" in sys.argv else None
d_index = sys.argv.index("-d") if "-d" in sys.argv else None


# Get file name
def get_filename() -> str | None:
    if f_index is None:
        return None

    if f_index + 1 >= len(sys.argv):
        raise ValueError("Filename is missing")

    filename = sys.argv[f_index + 1]

    if "." not in filename:
        raise ValueError("Filename must have extension")

    return filename


# Get path
def get_path() -> str | None:
    if d_index is None:
        return None

    if d_index + 1 >= len(sys.argv):
        return None

    if sys.argv[d_index + 1] == "-f":
        return None

    if f_index is not None:
        return os.path.join(*sys.argv[d_index + 1 : f_index])

    return os.path.join(*sys.argv[d_index + 1 :])


# Create directories
def create_path() -> str | None:
    if not flags_in_arg():
        raise ValueError("Pass -d flag to create path and -f flag to create file")

    path = get_path()

    if path is not None:
        return os.makedirs(path, exist_ok=True)


# Main logic
def file_editor() -> None:
    if get_path() is not None:
        create_path()

    file_name = get_filename()
    path = get_path()
    file_path = os.path.join(path, file_name) if path else file_name

    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        row_number = 1
        while True:
            content = input()
            if content == "stop":
                break
            file.write(f"{row_number} {content.strip()}\n")
            row_number += 1


file_editor()
