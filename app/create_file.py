from datetime import datetime
import os
import sys


def parse_arguments(args: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    index = 1
    while index < len(args):
        current_arg = args[index]
        if current_arg == "-d":
            index += 1
            while index < len(args) and not args[index].startswith("-"):
                directories.append(args[index])
                index += 1
            continue
        if current_arg == "-f":
            index += 1
            if index < len(args) and not args[index].startswith("-"):
                file_name = args[index]
                index += 1
            continue
        index += 1
    return directories, file_name


def get_content_lines() -> list[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def format_file_content(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [timestamp]
    for line_number, line in enumerate(lines, start=1):
        formatted_lines.append(f"{line_number} {line}")
    return "\n".join(formatted_lines)


def main() -> None:
    directories, file_name = parse_arguments(sys.argv)

    directory_path = ""
    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

    if file_name is not None:
        if directory_path:
            target_file_path = os.path.join(directory_path, file_name)
        else:
            target_file_path = file_name

        lines = get_content_lines()
        new_block = format_file_content(lines)

        file_exists = (
            os.path.exists(target_file_path)
            and os.path.getsize(target_file_path) > 0
        )
        mode = "a" if file_exists else "w"

        with open(target_file_path, mode, encoding="utf-8") as target_file:
            if file_exists:
                target_file.write(f"\n\n{new_block}")
            else:
                target_file.write(new_block)


if __name__ in ("__main__", "<run_path>"):
    main()
