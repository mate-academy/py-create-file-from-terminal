import os
import sys
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        if f.tell() == 0:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        for i, line in enumerate(iter(input, "stop"), 1):
            f.write(f"{i} {line}\n")

    if "-d" in sys.argv:
        dir_path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)
    else:
        print("Error: -f flag is missing")
        sys.exit(1)
