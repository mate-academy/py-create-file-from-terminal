import os
from datetime import datetime
import sys


def create_file(path: str, file_name: str, content: str) -> None:
    if len(path):
        os.makedirs(path, exist_ok=True)

    file_path = os.path.getsize(path, file_name) if path else file_name

    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for index, line in enumerate(content.splitlines()):
            file.write(f"{index + 1} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    print(args)

    file_name = None
    directory = []

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if "-d" in args:
        d_index = args.index("-d")
        if d_index + 1 < len(args):
            dir_parts = []
            i = d_index + 1
            while i < len(args) and args[i] != "-f":
                dir_parts.append(args[i])
                i += 1
            if dir_parts:
                directory = os.path.join(*dir_parts)

    content = ""
    if file_name:
        user_answers = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            user_answers.append(line)
        content = "\n".join(user_answers)

    if len(directory):
        create_file(os.path.join(directory), file_name, content)
    else:
        create_file("./", file_name, content)


if __name__ == "__main__":
    main()
