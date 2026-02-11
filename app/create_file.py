import os
import sys
from datetime import datetime


def create_directory(args: list) -> str:
    """Parses arguments for -d and creates directories."""
    if "-d" not in args:
        return ""

    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        directories = args[d_index + 1: f_index]
    else:
        directories = args[d_index + 1:]

    if directories:
        full_path = os.path.join(*directories)
        os.makedirs(full_path, exist_ok=True)
        return full_path

    return ""


def get_filename(args: list) -> str | None:
    """Parses arguments for -f and returns filename."""
    if "-f" not in args:
        return None

    f_index = args.index("-f")

    # Перевірка на помилку тут, винесена з main
    if f_index + 1 >= len(args):
        print("Error: provide a filename after -f")
        sys.exit(1)

    return args[f_index + 1]


def write_content_to_file(file_path: str) -> None:
    """Handles writing content and timestamp to the file."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.seek(0, 2)
        if file.tell() > 0:
            file.write("\n")

        file.write(f"{current_time}\n")

        page_count = 1
        while True:
            message = input("Enter content line: ")
            if message == "stop":
                break
            file.write(f"{page_count} {message}\n")
            page_count += 1


def main() -> None:
    args = sys.argv
    current_dir = create_directory(args)
    file_name = get_filename(args)

    if file_name:
        full_file_path = os.path.join(current_dir, file_name)
        write_content_to_file(full_file_path)


if __name__ == "__main__":
    main()

# --- TEST EVIDENCE ---
# I have manually tested the script with the following commands:
#
# 1. python app/create_file.py -d dir1 dir2
#    Result: Created folder "dir1" with subfolder "dir2". No file created.
#
# 2. python app/create_file.py -f test.txt
#    Result: Created "test.txt" in root. Added timestamp and content correctly.
#
# 3. python app/create_file.py -d dir1 dir2 -f file.txt
#    Result: Created directories and "file.txt" inside "dir1/dir2".
#
# 4. python app/create_file.py -f
#    Result: Printed "Error: provide a filename after -f" and exited.
# ---------------------