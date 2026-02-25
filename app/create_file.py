import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        end_index = args.index("-f") if "-f" in args else len(args)
        dirs = args[d_index + 1:end_index]
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if file_name:
        full_path = os.path.join(dir_path, file_name)
        content_lines = []

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file_exists_and_not_empty = (
            os.path.exists(full_path) and os.path.getsize(full_path) > 0
        )

        with open(full_path, "a") as f:
            if file_exists_and_not_empty:
                f.write("\n")
            f.write(f"{timestamp}\n")
            for i, line in enumerate(content_lines, 1):
                f.write(f"{i} {line}\n")


if __name__ == "__main__":
    create_file()
