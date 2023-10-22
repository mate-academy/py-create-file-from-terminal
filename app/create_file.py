import os
import sys
from datetime import datetime


def make_dir(directory_path: list) -> str:
    directory_path = os.path.join(*directory_path)
    try:
        os.makedirs(directory_path)
    except FileExistsError:
        print(f"Directory already exists: {directory_path}")
    return directory_path


def make_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Content Enter or stop")
        for counter, line in enumerate(iter(input, "stop")):
            print(f"{counter + 1} {line}\n")


def main() -> None:
    if "-f" in sys.argv and "-d" in sys.argv:
        directory_path = make_dir(
            sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]
        )
        file_name = sys.argv[sys.argv.index("-f") + 1]
        make_file(file_name, directory_path)

    elif "-d" in sys.argv:
        make_dir(sys.argv[sys.argv.index("-d") + 1:])

    elif "-f" in sys.argv:
        make_file(sys.argv[sys.argv.index("-f") + 1])


if __name__ == "__main__":
    main()
