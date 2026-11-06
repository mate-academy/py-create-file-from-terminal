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

    if has_file:
        file_index: int = sys.argv.index("-f")
        directories = sys.argv[directory_index + 1 : file_index]
    else:
        directories = sys.argv[directory_index + 1 :]

if has_directory:
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
else:
    print("Please provide -f flag")
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


with open(file_path, "a", encoding="utf-8") as file:
    file.write(timestamp + "\n")

    for number, line in enumerate(content_lines, start=1):
        file.write(f"{number} {line}\n")


print(f"Content successfully saved to {file_path}")
