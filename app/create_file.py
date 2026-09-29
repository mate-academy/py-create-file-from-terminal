import os
import sys
from datetime import datetime


def get_content() -> list[str]:
    content = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content.append(line)

    return content


def write_to_file(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")

        for index, line in enumerate(content, start=1):
            file.write(f"{index} {line}\n")

        file.write("\n")


def main() -> None:
    args = sys.argv[1:]

    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1

        if "-f" in args:
            f_index = args.index("-f")
            directory_parts = args[d_index:f_index]
        else:
            directory_parts = args[d_index:]

    if "-f" in args:
        f_index = args.index("-f") + 1

        if f_index < len(args):
            file_name = args[f_index]

    directory_path = os.path.join(*directory_parts) if directory_parts else ""

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is not None:
        file_path = os.path.join(directory_path, file_name)
        content = get_content()
        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
