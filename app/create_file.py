import sys
import os
import datetime


def parse_args() -> tuple:
    directory_parts = []
    file_name = None

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        if "-f" in sys.argv:
            directory_parts = sys.argv[dir_index: sys.argv.index("-f")]
        else:
            directory_parts = sys.argv[dir_index:]

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]

    return directory_parts, file_name


def create_directory(directory_parts: list) -> str:
    if not directory_parts:
        return os.getcwd()
    directory_path = os.path.join(os.getcwd(), *directory_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(file_path: str) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    file_exists_and_not_empty = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )
    with open(file_path, "a", encoding="utf-8") as source_file:
        if file_exists_and_not_empty:
            source_file.write("\n")
        source_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            source_file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    directory_parts, file_name = parse_args()

    if directory_parts:
        directory_path = create_directory(directory_parts)
    else:
        directory_path = os.getcwd()

    if file_name:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
