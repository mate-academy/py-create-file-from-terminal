import os
import sys
from datetime import datetime


def create_file(file_path: str, content: str) -> None:
    with open(file_path, "a") as file:
        file.write(content)


def main() -> None:
    path = "."
    if sys.argv[1] == "-d":
        directory_path = sys.argv[2:] if "-f" != sys.argv[-2] else sys.argv[2:-2]
        path = os.path.join(*directory_path)
    elif sys.argv[1] == "-f" and "-d" in sys.argv:
        path = os.path.join(*sys.argv[4:])

    if path:
        os.makedirs(path, exist_ok=True)

    if "-f" in sys.argv:
        path = os.path.join(path, sys.argv[sys.argv.index("-f") + 1])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_file(path, f"\n{timestamp}")

        line_number = 1
        while True:
            line = input(
                f"{line_number} Enter content line (type 'stop' to finish): "
            )
            if line == "stop":
                break
            create_file(path, f"\n{line_number} {line}")
            line_number += 1


if __name__ == "__main__":
    main()
