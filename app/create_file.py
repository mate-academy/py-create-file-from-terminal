import os
import sys
from datetime import datetime
from typing import List


def create_file(directory: List[str], filename: str,
                content: List[str]) -> None:
    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)
        if filename:
            filename = os.path.join(directory_path, filename)

    if filename:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content_with_timestamp = f"{timestamp}\n"

        with open(filename, "a") as f:
            if os.path.exists(filename):
                f.write("\n")
            else:
                f.write(content_with_timestamp)
            line_number = 1
            for line in content:
                if line == "stop":
                    break
                f.write(f"{line_number} {line}\n")
                line_number += 1


def parse_arguments() -> tuple:
    args = sys.argv[1:]
    if "-d" in args:
        flag_index = args.index("-d")
        directory = args[flag_index + 1:args.index("-f")] \
            if "-f" in args else args[flag_index + 1:]
    else:
        directory = []

    if "-f" in args:
        flag_index = args.index("-f")
        filename = args[flag_index + 1]
        content = args[flag_index + 2:] if flag_index + 2 < len(args) else []
    else:
        filename = ""
        content = []

    return directory, filename, content


def main() -> None:
    directory, filename, content = parse_arguments()
    create_file(directory, filename, content)


if __name__ == "__main__":
    main()
