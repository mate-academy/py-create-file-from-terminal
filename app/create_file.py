import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    if len(args) < 1:
        print("Error")
        return

    create_dirs = "-d" in args
    create_file = "-f" in args

    dir_list = []

    if "-d" in args:
        d_index = args.index("-d")

        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                continue

            if create_file and arg == args[-1]:
                break

            dir_list.append(arg)

    file_name = args[-1]

    if dir_list:
        result_dir = os.path.join(*dir_list)
    else:
        result_dir = ""

    if create_dirs and result_dir:
        os.makedirs(result_dir, exist_ok=True)
        print("Folder created!")

    if not create_file:
        return

    if result_dir:
        file_path = os.path.join(result_dir, file_name)
    else:
        file_path = file_name

    now = datetime.now()
    timestamp = now.strftime("%d.%m.%Y %H:%M:%S")

    parent_dir = os.path.dirname(file_path)

    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)

    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"

    with open(file_path, mode, encoding="utf-8") as f:
        f.write(f"{timestamp}\n")

        line = 1

        while True:
            content = input("Enter content line: ")

            if content.lower() == "stop":
                break

            f.write(f"{line} {content}\n")
            line += 1


if __name__ == "__main__":
    main()