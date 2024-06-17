import os
import sys
from datetime import datetime


def resolve_directory() -> str:
    if "-f" in sys.argv:
        end_index = sys.argv.index("-f")
    else:
        end_index = len(sys.argv)

    directory_arguments = sys.argv[sys.argv.index("-d") + 1:end_index]
    directory_path = os.path.join(*directory_arguments)

    os.makedirs(directory_path, exist_ok=True)

    if not directory_path.endswith(os.path.sep):
        directory_path += os.path.sep

    return str(directory_path)


def resolve_file(file_path: str) -> None:
    file_path += sys.argv[-1]

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        numerator = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{numerator} {line}\n")
            numerator += 1


if __name__ == "__main__":
    path = ""
    if "-d" in sys.argv:
        path = resolve_directory()

    if "-f" in sys.argv:
        resolve_file(path)
