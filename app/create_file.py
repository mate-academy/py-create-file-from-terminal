import os
import sys
from datetime import datetime
from typing import cast


def parse_args(args: list[str]) -> tuple[str | None, str | None]:
    directory_path: str | None = None
    file_name: str | None = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts: list[str] = []

        for part in args[d_index + 1:]:
            if part.startswith("-"):
                break
            dir_parts.append(part)

        if dir_parts:
            directory_path = cast(str, os.path.join(*dir_parts))

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    return directory_path, file_name


def main() -> None:
    args = sys.argv[1:]
    directory_path, file_name = parse_args(args)

    if file_name is None:
        print("Error: you need to transfer the file using the "
              "-f filename flag.")
        return

    if directory_path is not None:
        os.makedirs(directory_path, exist_ok=True)

    full_path = (
        os.path.join(directory_path, file_name)
        if directory_path
        else file_name
    )

    if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
        with open(full_path, "a", encoding="utf-8") as source_file:
            source_file.write("\n")

    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a", encoding="utf-8") as source_file:
        source_file.write(timestamp + "\n")

        line_number = 1
        for line in lines:
            source_file.write(f"{line_number} {line}\n")
            line_number += 1

        source_file.write("\n")


if __name__ == "__main__":
    main()
