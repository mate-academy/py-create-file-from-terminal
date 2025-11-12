import sys
import os
from datetime import datetime


def create_directory(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.exists(file_path):
            if os.path.getsize(file_path) > 0:
                file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        i = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{i} {line}\n")
            i += 1


def main() -> None:
    args = sys.argv[1:]
    if not args:
        return

    path = ""

    if "-d" in args:
        d_index = args.index("-d")
        path_parts = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            path_parts.append(arg)
        path = create_directory(path_parts)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
            file_path = os.path.join(path, file_name) if path else file_name
            create_file(file_path)


if __name__ == "__main__":
    main()
