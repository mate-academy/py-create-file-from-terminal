import os
import sys
from typing import Any
from datetime import datetime


def writing(filename: Any) -> None:
    count = 0
    filename.write(datetime.now().isoformat() + "\n")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        count += 1
        filename.write(f"{count} {line}\n")


def f_command(filename: str) -> None:
    mode = "a" if os.path.exists(filename) else "w"
    with open(filename, mode) as file:
        writing(file)


def d_command(dirs: list[str]) -> None:
    str_dirs = os.path.join(*dirs)
    os.makedirs(str_dirs, exist_ok=True)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        d_idx = sys.argv.index("-d")
        f_idx = sys.argv.index("-f")
        dirs = sys.argv[d_idx + 1:f_idx]
        filename = sys.argv[f_idx + 1]

        if len(dirs) == 1:
            os.mkdir(dirs[0])
            str_dirs = dirs[0]
        else:
            d_command(dirs)

        file_path = os.path.join(str_dirs, filename)
        f_command(file_path)

    elif "-f" in sys.argv:
        f_command(sys.argv[sys.argv.index("-f") + 1])

    elif "-d" in sys.argv:
        d_idx = sys.argv.index("-d")
        dirs = sys.argv[d_idx + 1:]
        d_command(dirs)


if __name__ == "__main__":
    main()
