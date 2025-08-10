import sys
import os
from datetime import datetime


def create_file():
    args = sys.argv[1:]
    dir_path = None
    file_name = None
    create_dir = False
    create_file = False

    if "-d" in args:
        create_dir = True
        d_index = args.index("-d")

        dir_items = []
        for item in args[d_index + 1:]:
            if item.startswith("-"):
                break
            dir_items.append(item)
        if dir_items:
            dir_path = os.path.join(*dir_items)
        else:
            print("Error: No folders specified after -d")
            return

    if "-f" in args:
        create_file = True
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Error: No file name specified after -f")
            return

    if create_dir and dir_path:
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory created: {dir_path}")
        except Exception as e:
            print(f"Error when creating directory: {e}")
            return

    if create_file and file_name:
        if create_dir and dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        lines_blocks = []
        while True:
            line_input = input("Enter content line: ")
            if line_input.strip().lower() == "stop":
                break
            lines_blocks.append(line_input)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        existing_content = ""
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                existing_content = f.read()

        new_block_lines = []

        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"\n{timestamp}\n")
            for idx, line in enumerate(lines_blocks, start=1):
                f.write(f"{idx} {line}\n")

        print(f"File '{file_path}' was successfully updated.")

if __name__ == "__main__":
    create_file()