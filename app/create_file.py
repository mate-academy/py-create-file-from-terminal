import os
import sys

from datetime import datetime
from pathlib import Path


def write_to_file(path_to_file: Path) -> None:
    write_mode = "w"
    if path_to_file.is_file():
        write_mode = "a"
    with open(file_name, write_mode) as file:
        if write_mode == "a":
            file.write("\n" + current_timestamp + "\n")
        else:
            file.write(current_timestamp + "\n")
        for counter, line in enumerate(
                iter(
                    lambda: input("Enter content line: "),
                    "stop"
                ),
                start=1):
            file.write(f"{counter} {line}\n")


if "-d" in sys.argv and "-f" not in sys.argv:
    parts = sys.argv[sys.argv.index("-d") + 1:]
    path = Path(os.getcwd(), *parts)
    path.mkdir(parents=True, exist_ok=True)
elif "-f" in sys.argv and "-d" not in sys.argv:
    current_timestamp = (datetime.now().
                         strftime("%Y-%m-%d %H:%M:%S"))  # current timestamp
    file_name = sys.argv[-1]
    path = Path(os.getcwd()) / file_name
    write_to_file(path)

elif "-f" in sys.argv and "-d" in sys.argv:
    current_timestamp = (datetime.now().
                         strftime("%Y-%m-%d %H:%M:%S"))  # current timestamp
    parts = sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
    path = Path(os.getcwd(), *parts)
    path.mkdir(parents=True, exist_ok=True)
    file_name = sys.argv[-1]
    file_path = path / file_name
    write_to_file(file_path)
