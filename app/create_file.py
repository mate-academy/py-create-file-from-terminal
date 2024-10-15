import os
import sys
from datetime import datetime


def create_file_with_content(file_path: str) -> None:
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.strip().lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1

        dir_path = os.path.join(*sys.argv[dir_index:file_index - 1])
        file_name = sys.argv[file_index]

        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, file_name)
        create_file_with_content(file_path)

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dir_path = os.path.join(*sys.argv[dir_index:])
        os.makedirs(dir_path, exist_ok=True)

        print(f"Directory '{dir_path}' created.")

    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]

        file_path = os.path.join(os.getcwd(), file_name)
        create_file_with_content(file_path)

    else:
        print(
            "Invalid arguments. Use -d for directory and -f for file creation."
        )
