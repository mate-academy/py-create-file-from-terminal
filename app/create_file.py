import os
import sys
from datetime import datetime


def create_file(
        directory: str,
        file_name: str,
        content_lines: list
) -> None:
    file_path = os.path.join(directory, file_name)
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [f"{datetime_now}\n"]

    for i, line in enumerate(content_lines, start=1):
        content.append(f"{i} {line}\n")

    with open(file_path, "a" if os.path.exists(file_path) else "w") as file:
        file.writelines(content)


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        dir_index = args.index("-d")
        directory = os.path.join(*args[dir_index + 1:])
        os.makedirs(directory, exist_ok=True)
    else:
        directory = ""

    if "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        content_lines = []
        print("Enter content lines (type 'stop' to finish):")

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)

        create_file(directory, file_name, content_lines)


if __name__ == "__main__":
    main()
