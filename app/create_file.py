import os
import sys
from datetime import datetime


def main(arguments: list[str] | None = None) -> None:
    arguments = sys.argv[1:] if arguments is None else arguments
    directory_flag = "-d" in arguments
    file_flag = "-f" in arguments

    if not directory_flag and not file_flag:
        raise SystemExit(
            "Usage: create_file.py [-d directories...] [-f filename]"
        )

    filename = None
    filename_index = None
    if file_flag:
        file_flag_index = arguments.index("-f")
        filename_index = file_flag_index + 1
        if (
            filename_index >= len(arguments)
            or arguments[filename_index].startswith("-")
        ):
            raise SystemExit("The -f flag requires a filename.")
        filename = arguments[filename_index]

    if not directory_flag and file_flag and len(arguments) > 2:
        raise SystemExit(
            "Unexpected arguments; use -d to specify directories."
        )

    directories = [
        argument
        for index, argument in enumerate(arguments)
        if argument not in {"-d", "-f"} and index != filename_index
    ]

    if directory_flag and directories:
        os.makedirs(os.path.join(*directories), exist_ok=True)

    if filename is None:
        return

    file_path = (
        os.path.join(*directories, filename)
        if directory_flag and directories
        else filename
    )
    existed = os.path.exists(file_path)
    with open(file_path, "a", encoding="utf-8"):
        pass

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    with open(file_path, "a", encoding="utf-8") as destination:
        if existed and os.path.getsize(file_path) > 0:
            with open(file_path, "rb") as existing_file:
                existing_file.seek(-1, os.SEEK_END)
                ends_with_newline = existing_file.read(1) == b"\n"
            destination.write("\n" if ends_with_newline else "\n\n")

        destination.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for number, line in enumerate(content_lines, start=1):
            destination.write(f"{number} {line}\n")


if __name__ in {"__main__", "<run_path>"}:
    main()
