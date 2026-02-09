import os
import sys
from datetime import datetime


def create_folder(args: list) -> str:
    if "-d" not in args:
        return ""

    start_index = args.index("-d") + 1
    end_index = args.index("-f") if "-f" in args[start_index:] else len(args)
    paths = args[start_index:end_index]
    path = os.path.join(*paths)

    os.makedirs(path, exist_ok=True)
    return path


def create_file(args: str) -> None:
    if "-f" not in args:
        return

    path = create_folder(args)
    file_name = os.path.join(path, args[args.index("-f") + 1])
    open_mode = "a" if os.path.exists(file_name) else "w"

    with open(file_name, open_mode) as file:
        if open_mode == "a":
            file.write("\n")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")

        line_count = 0
        while True:
            line_count += 1
            line_input = input("Enter content line: ")
            if line_input == "stop":
                break
            file.write(f"{line_count} {line_input}\n")


def main() -> None:
    arguments = sys.argv
    create_file(arguments)


if __name__ == "__main__":
    main()
