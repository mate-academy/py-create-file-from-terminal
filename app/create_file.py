import sys
import os
import datetime
from typing import Any


def parse_argument() -> Any:
    folder_name = []
    file_name = None
    idx_f = sys.argv.index("-f") if "-f" in sys.argv else None
    idx_d = sys.argv.index("-d") if "-d" in sys.argv else None

    if idx_f is not None:
        file_name = sys.argv[idx_f + 1]

    if idx_d is not None:
        if idx_f is not None and idx_f > idx_d:
            end_idx = idx_f
        else:
            end_idx = len(sys.argv)

        folder_name = sys.argv[idx_d + 1 : end_idx]

    return folder_name, file_name


def create_dir(folder_name: list[Any], file_name: Any) -> str | Any:
    target_dir = ""
    if folder_name:
        target_dir = os.path.join("./", *folder_name)
        os.makedirs(target_dir, exist_ok=True)

    if file_name:
        return os.path.join(target_dir, file_name)
    return None


def get_content() -> list:
    content = []
    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content.append(line)

    return content


def write_to_file(final_path: Any, content: Any) -> None:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(final_path, "a") as file:
        file.write(now + "\n")

        for index, line in enumerate(content, start=1):
            file.write(f"{index} {line}\n")

        file.write("\n")


def main() -> None:

    folders, file_name = parse_argument()
    path = create_dir(folders, file_name)
    if path:
        content = get_content()

        if content:
            write_to_file(path, content)


if __name__ == "__main__":
    main()
