import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    if "-d" in args and "-f" in args:
        d_idx = args.index("-d")
        f_idx = args.index("-f")

        if d_idx < f_idx:
            dir_parts = args[d_idx + 1:f_idx]
            file_name = args[f_idx + 1]
        else:
            file_name = args[f_idx + 1]
            dir_parts = args[d_idx + 1:]

    elif "-d" in args:
        d_idx = args.index("-d")
        dir_parts = args[d_idx + 1:]

    elif "-f" in args:
        f_idx = args.index("-f")
        file_name = args[f_idx + 1]

    dir_path = os.path.join(*dir_parts) if dir_parts else ""

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content_lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        formatted_text = [timestamp]
        for index, line in enumerate(content_lines, start=1):
            formatted_text.append(f"{index} {line}")

        file_path = (
            os.path.join(dir_path, file_name) if dir_path else file_name
        )

        file_exists = os.path.exists(file_path)

        with open(file_path, "a", encoding="utf-8") as file:
            if file_exists:
                file.write("\n\n")
            file.write("\n".join(formatted_text))


create_file()
