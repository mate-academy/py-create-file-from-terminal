import os
import sys
from datetime import datetime


def create_path(path_parts: list) -> None:
    path_dir = os.path.join(*path_parts)
    try:
        os.makedirs(path_dir, exist_ok=True)
    except OSError as e:
        print(f"Failed to create directory '{path_dir}': {e}")


def create_content(file_name: str) -> None:
    style = "a" if os.path.exists(file_name) else "w"
    with open(file_name, style) as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_number = 1
        while True:
            line_content = input(f"Enter content line {line_number}: ")
            if line_content.lower() == "stop":
                break
            file.write(f"{line_number} {line_content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("No arguments provided. Use '-d' for directory and '-f' for file.")
        return

    path_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if d_index + 1 < len(args) and args[d_index + 1] != "-f":
            if "-f" in args:
                f_index = args.index("-f")
                path_parts = args[d_index + 1:f_index]
                if f_index + 1 < len(args):
                    file_name = args[f_index + 1]
                else:
                    print("No file name provided after '-f'")
                    return
            else:
                path_parts = args[d_index + 1:]
        else:
            print("No directory provided after '-d'")
            return

    elif "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("No file name provided after '-f'")
            return

    if path_parts:
        create_path(path_parts)

    if file_name:
        file_path = os.path.join(*path_parts, file_name) if path_parts else file_name
        create_content(file_path)


if __name__ == "__main__":
    main()
