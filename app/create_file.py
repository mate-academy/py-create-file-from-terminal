import os
import sys
from datetime import datetime, timezone, timedelta

TIME_ZONE_OFFSET = timezone(timedelta(hours=3))


def get_arguments() -> tuple:
    arguments = sys.argv
    directory_names = []
    file_name = ""

    if "-d" in arguments:
        d_index = arguments.index("-d")
        for arg in arguments[d_index + 1:]:
            if arg.startswith("-"):
                break
            directory_names.append(arg)

    if "-f" in arguments:
        f_index = arguments.index("-f")
        if f_index + 1 < len(arguments):
            file_name = arguments[f_index + 1]

    return directory_names, file_name


def get_content() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def save_to_file(directory_names: list, file_name: str, content_lines: list) \
        -> None:
    full_path = ""
    if directory_names:
        full_path = os.path.join(*directory_names)
        os.makedirs(full_path, exist_ok=True)

    if not file_name:
        return

    target_file = os.path.join(full_path, file_name)

    with open(target_file, "a") as output_file:
        now = datetime.now(TIME_ZONE_OFFSET)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        output_file.write(f"{timestamp}\n")

        for i, line in enumerate(content_lines, 1):
            output_file.write(f"{i} {line}\n")

        output_file.write("\n")


def main() -> None:
    folder_parts, name = get_arguments()

    if not folder_parts and not name:
        return

    if folder_parts and not name:
        os.makedirs(os.path.join(*folder_parts), exist_ok=True)
        return

    lines = get_content()
    save_to_file(folder_parts, name, lines)


if __name__ == "__main__":
    main()
