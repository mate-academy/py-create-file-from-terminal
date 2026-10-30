import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")

            if d_index < f_index:
                directory_parts = args[d_index + 1:f_index]
            else:
                directory_parts = args[d_index + 1:]
        else:
            directory_parts = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")

        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if not file_name:
        return

    file_path = (
        os.path.join(directory_path, file_name)
        if directory_path
        else file_name
    )

    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(file_path)

    with open(file_path, "a" if file_exists else "w") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for number, line in enumerate(content_lines, start=1):
            file.write(f"{number} {line}\n")


if __name__ == "__main__":
    main()
