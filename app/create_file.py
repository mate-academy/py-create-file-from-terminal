import os
import sys
from datetime import datetime


def create_app() -> None:
    args = sys.argv[1:]

    path_parts = []
    file_name = None

    f_flag_present = "-f" in args

    current_flag = None
    for arg in args:
        if arg == "-d":
            current_flag = "-d"
            continue
        elif arg == "-f":
            current_flag = "-f"
            continue

        if current_flag == "-d":
            path_parts.append(arg)
        elif current_flag == "-f":
            file_name = arg
            current_flag = None

    if f_flag_present and file_name is None:
        print("Error: '-f' flag provided but no filename given.")
        sys.exit(1)

    full_path = os.path.join(*path_parts) if path_parts else "."

    if path_parts:
        os.makedirs(full_path, exist_ok=True)

    if file_name:
        file_full_path = os.path.join(full_path, file_name)

        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_full_path, "a", encoding="utf-8") as f:
            f.write(f"{timestamp}\n")
            for i, line in enumerate(content_lines, 1):
                f.write(f"{i} {line}\n")
            f.write("\n")


if __name__ == "__main__":
    create_app()
