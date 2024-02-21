import os
import sys
from datetime import datetime


def main() -> None:
    dir_path = None
    file_name = None

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1

        dir_path = os.path.join(*sys.argv[dir_index : sys.argv.index("-f")])

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(dir_path,
                                 file_name) if dir_path else file_name
        append_to_file(file_path)


def append_to_file(file_path: os.path) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as f:

        if file_exists:
            f.write("\n")

        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_num = 1

        print("Enter content line (or 'stop' to finish):")

        while True:
            line = input()
            if line == "stop":
                break

            f.write(f"{line_num} {line}\n")
            line_num += 1


if __name__ == "__main__":
    main()
