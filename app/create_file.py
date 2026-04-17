import os
import sys
from datetime import datetime


def create_app() -> None:
    args = sys.argv[1:]

    try:
        d_idx = args.index("-d") if "-d" in args else None
        f_idx = args.index("-f") if "-f" in args else None
    except ValueError:
        print("Error: Invalid arguments.")
        return

    path_parts = []
    file_name = ""

    if d_idx is not None:
        end_d = f_idx if f_idx is not None and f_idx > d_idx else len(args)
        path_parts = args[d_idx + 1:end_d]

    if f_idx is not None:
        file_name = args[f_idx + 1]

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


if __name__ == "__main__":
    create_app()
