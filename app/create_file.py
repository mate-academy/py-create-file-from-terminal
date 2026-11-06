import sys
import os
from datetime import datetime

has_directory: bool = "-d" in sys.argv
has_file: bool = "-f" in sys.argv

if not has_directory and not has_file:
    print("Please provide -d or -f flag")
    sys.exit(1)


directories: list[str] = []

if has_directory:
    directory_index: int = sys.argv.index("-d")

    next_flag_index: int = len(sys.argv)

    for index, argument in enumerate(
        sys.argv[directory_index + 1 :], start=directory_index + 1
    ):
        if argument.startswith("-"):
            next_flag_index = index
            break

    directories = sys.argv[directory_index + 1 : next_flag_index]

    if not directories:
        print("Please provide directory names")
        sys.exit(1)

    directory_path: str = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)

else:
    directory_path = ""


if has_file:
    file_index: int = sys.argv.index("-f")

    if file_index + 1 >= len(sys.argv):
        print("Please provide file name")
        sys.exit(1)

    file_name: str = sys.argv[file_index + 1]

    if file_name.startswith("-"):
        print("Please provide a valid file name")
        sys.exit(1)

    file_path: str = os.path.join(directory_path, file_name)

    content_lines: list[str] = []

    while True:
        line: str = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    current_time: datetime = datetime.now()
    timestamp: str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    file_exists: bool = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        file.write(timestamp + "\n")

        for number, line in enumerate(content_lines, start=1):
            file.write(f"{number} {line}\n")

    print(f"Content successfully saved to {file_path}")
