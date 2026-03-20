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


# Get flag index
def get_flag_index(args: list[str]) -> tuple[int | None, int, None]:
    f_index = args.index("-f") if "-f" in args else None
    d_index = args.index("-d") if "-d" in args else None
    return (f_index, d_index)


# Get file name
def get_filename(args: list[str], f_index: int | None) -> str:

    if f_index is None:
        return None

    if f_index + 1 >= len(args):
        raise ValueError("Filename is missing")

    filename = args[f_index + 1]

    if "." not in filename:
        raise ValueError("Filename must have extension")

    return filename


# Get path
def get_path(args: list[str], f_index: int, d_index: int) -> str | None:
    if d_index is None:
        return None

    if d_index + 1 >= len(args):
        return None

    if sys.argv[d_index + 1] == "-f":
        return None

    if f_index is not None:
        return os.path.join(*args[d_index + 1 : f_index])

    return os.path.join(*args[d_index + 1 :])


# Create directories
def create_path(path: str | None) -> None:
    if path is not None:
        os.makedirs(path, exist_ok=True)


# Write content
def write_content(file_path: str) -> None:
    if not flags_in_arg():
        raise ValueError("Pass at least 1 flag to arguments")
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        row_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"{row_number} {content.strip()}\n")
            row_number += 1


# Main logic
def file_editor() -> None:
    args = sys.argv
    f_index, d_index = get_flag_index(args)
    path = get_path(args, f_index, d_index)
    file_name = get_filename(args, f_index)

    create_path(path)

    if file_name is None:
        return

    file_path = os.path.join(path, file_name) if path else file_name
    write_content(file_path)


file_editor()
