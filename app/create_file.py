import sys
import os
import datetime
from typing import Any, Generator


def parse_arguments(args: list[str]) -> tuple[list[Any], Any | None]:
    dir_parts = []
    file_name = None
    mode = None

    for arg in args:
        if arg == "-d":
            mode = "dir"
        elif arg == "-f":
            mode = "file"
        else:
            if mode == "dir":
                dir_parts.append(arg)
            elif mode == "file":
                file_name = arg

    return dir_parts, file_name


def get_file_content() -> Generator[tuple[int, str], Any, None]:
    line_count = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        yield line_count, line
        line_count += 1


def main() -> None:
    args = sys.argv[1:]
    dir_parts, file_name = parse_arguments(args)

    if not file_name:
        sys.exit(1)

    if dir_parts:
        target_directory = os.path.join(os.getcwd(), *dir_parts)
        os.makedirs(target_directory, exist_ok=True)
    else:
        target_directory = os.getcwd()

    file_path = os.path.join(target_directory, file_name)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as f:
        if file_exists:
            f.write("\n\n")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + "\n")

        for number, line in get_file_content():
            f.write(f"{number} {line}\n")

    print(f"Content written to {file_path}")


if __name__ == "__main__":
    main()
