from typing import Any
import datetime
import os
import sys


def create_file(*args: Any) -> None:

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


def create_folder(path: list) -> str:
    os.makedirs(os.path.join(*path))
    return os.path.join(*path)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        if sys.argv.index("-d") < sys.argv.index("-f"):
            path = create_folder(
                sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
            )
        else:
            path = create_folder(
                sys.argv[sys.argv.index("-d") + 1:]
            )
        file_name = "".join(sys.argv[sys.argv.index("-f") + 1])
        create_file(path, file_name)
    elif "-d" in sys.argv:
        path = sys.argv[sys.argv.index("-d") + 1:]
        create_folder(path)
    elif "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1:]
        create_file("".join(file_name))


if __name__ == "__main__":
    main()
