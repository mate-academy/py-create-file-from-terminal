import os
import sys

from datetime import datetime
from pathlib import Path


def file_consist(name: str) -> None:
    with open(file_name, "a") as file:
        file.write("\n" + current_timestamp + "\n")
        for counter, line in enumerate(
                iter(
                    lambda: input("Enter content line: "),
                    "stop"
                ),
                start=1):
            file.write(f"{counter} {line}\n")


def file_not_consist(name: str) -> None:
    with open(file_name, "w") as file:
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
    path = Path(os.getcwd(), file_name)
    if path.is_file():
        file_consist(file_name)
        file_not_consist(file_name)

    else:
        file_not_consist(file_name)

elif "-f" in sys.argv and "-d" in sys.argv:
    current_timestamp = (datetime.now().
                         strftime("%Y-%m-%d %H:%M:%S"))  # current timestamp
    parts = sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
    path = Path(os.getcwd(), *parts)
    path.mkdir(parents=True, exist_ok=True)
    os.chdir(path)
    file_name = sys.argv[-1]
    file_not_consist(file_name)
