import sys
import os
from datetime import datetime


def get_arg_value(flag: str) -> str | None:
    try:
        index = sys.argv.index(flag)
        value = sys.argv[index + 1]
        if value.startswith("-"):
            return None
        return value
    except (ValueError, IndexError):
        return None


def create_file() -> None:
    dir_path = get_arg_value("-d")
    file_name = get_arg_value("-f")

    if file_name is None:
        print("Error: Missing file name after '-f'.")
        return

    if dir_path:
        if not os.path.isabs(dir_path):  # Validate directory path
            dir_path = os.path.abspath(dir_path)
        try:
            os.makedirs(dir_path, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory: {e}")
            return

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    try:
        with open(file_path, "a") as file:
            file.write(f'\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            line_number = 0
            while True:
                line = input("Enter content line (type 'stop' to finish): ")
                if line.lower() == "stop":
                    break
                line_number += 1
                file.write(f"\n{line_number} {line}")
        print(f"File saved at: {file_path}")
    except OSError as e:
        print(f"File error: {e}")
