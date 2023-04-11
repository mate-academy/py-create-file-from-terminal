from typing import Any
import datetime
import os
import sys


def file_creates(*args: Any) -> None:

    with open(os.path.join(*args), "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        count = 1
        content = None
        while content != "stop":
            content = input("Enter content line: ")
            if content == "stop":
                break
            f.write(f"{count} {content}\n")
            count += 1


def folder_create(path: list) -> str:
    os.makedirs(os.path.join(*path))
    return os.path.join(*path)


def creates() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = folder_create(
            sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        )
        file_name = "".join(sys.argv[sys.argv.index("-f") + 1:])
        file_creates(path, file_name)
    elif "-d" in sys.argv:
        path = sys.argv[sys.argv.index("-d") + 1:]
        folder_create(path)
    elif "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1:]
        file_creates("".join(file_name))


if __name__ == "__main__":
    creates()
