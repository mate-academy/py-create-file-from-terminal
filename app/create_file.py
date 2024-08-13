import os
import sys
from datetime import datetime


def path_handler(file_name: str | None, path: str | None) -> None:
    if path:
        os.makedirs(path, exist_ok=True)
    else:
        path = ""

    if file_name:

        file_output = get_file_output()

        try:
            with open(os.path.join(path, file_name), "a") as file:
                file.writelines(file_output)
        except FileNotFoundError as e:
            print(f"File does not exist: {e}")
        except PermissionError as e:
            print(f"You do not have permission: {e}")


def get_file_output():
    file_output = [f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
    file_output.extend(get_user_input())
    file_output.append("\n")
    return file_output


def get_user_input():
    lines = []
    n_line = 1

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(f"{n_line} {line}\n")
        n_line += 1

    return lines


def get_arguments(args):
    file_name = None
    path = None

    if "-d" in args:
        path = ""
        i = args.index("-d") + 1

        while i < len(args) and not args[i].startswith("-"):
            path = os.path.join(path, args[i])
            i += 1

    if "-f" in args:
        file_name = args[args.index("-f") + 1]

    return file_name, path


if __name__ == "__main__":
    args = sys.argv

    file_name, path = get_arguments(args)

    path_handler(file_name, path)
