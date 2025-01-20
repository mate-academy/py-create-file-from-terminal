import sys
import os
from datetime import datetime
from typing import List, Optional


def parse_arguments(min_args: int) -> None:
    if len(sys.argv) < min_args:
        print("Error: Not enough arguments.")
        sys.exit(1)


def parse_flags() -> tuple[Optional[List[str]], Optional[str]]:
    dir_path = None
    file_name = None

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dir_path = sys.argv[d_index + 1:]

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]

    return dir_path, file_name


def create_directory_and_file(
        dir_path: Optional[List[str]],
        file_name: Optional[str]
) -> None:

    if dir_path:
        os.makedirs(os.path.join(*dir_path), exist_ok=True)

    if file_name:

        with open(file_name, "a") as f:

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")
            line_num = 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                f.write(f"{line_num} {line}\n")
                line_num += 1


def main() -> None:

    parse_arguments(3)

    dir_path, file_name = parse_flags()

    create_directory_and_file(dir_path, file_name)


if __name__ == "__main__":
    main()


