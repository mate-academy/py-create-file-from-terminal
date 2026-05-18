import sys
import os
from datetime import datetime

current_dir = os.getcwd()

filename = None
directories = []

directory_path = None

d_exists = "-d" in sys.argv
f_exists = "-f" in sys.argv

d_index = sys.argv.index("-d") if d_exists else None
f_index = sys.argv.index("-f") if f_exists else None

filename = None
directories = []

if d_exists and f_exists:
    if d_index < f_index:
        directories = sys.argv[d_index + 1:f_index]
        filename = sys.argv[f_index + 1]
    else:
        filename = sys.argv[f_index + 1]
        directories = sys.argv[d_index + 1:]

elif d_exists:
    directories = sys.argv[d_index + 1:]

elif f_exists:
    filename = sys.argv[f_index + 1]

directory_path = os.path.join(
    current_dir,
    *directories
) if directories else current_dir

if directories:
    os.makedirs(directory_path, exist_ok=True)

full_path = os.path.join(
    directory_path,
    filename
)if filename else None


def create_file(full_path: str, lines: list[str]) -> None:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = ""

    for index, line in enumerate(lines, start=1):
        content += f"{index} {line}\n"

    with open(full_path, "a") as file:
        if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
            file.write("\n")
        file.write(timestamp + "\n")
        file.write(content)


if filename:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    create_file(full_path, lines)
