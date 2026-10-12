from datetime import datetime
import os
import sys

args = sys.argv[1:]

dirs = []
filename = None

i = 0
while i < len(args):
    if args[i] == "-d":
        i += 1
        while (
            i < len(args)
            and not args[i].startswith("-")
        ):
            dirs.append(args[i])
            i += 1
    elif args[i] == "-f":
        i += 1
        if i < len(args):
            filename = args[i]
            i += 1
    else:
        i += 1

target_dir = ""
if dirs:
    target_dir = os.path.join(*dirs)
    os.makedirs(target_dir, exist_ok=True)

if filename:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    formatted_lines = [timestamp]
    for idx, line_item in enumerate(
        lines, start=1
    ):
        formatted_lines.append(f"{idx} {line_item}")

    new_entry = "\n".join(formatted_lines)

    if target_dir:
        full_file_path = os.path.join(
            target_dir, filename
        )
    else:
        full_file_path = filename

    existing_content = ""
    if os.path.exists(full_file_path):
        with open(
            full_file_path,
            "r",
            encoding="utf-8"
        ) as f:
            existing_content = f.read().rstrip("\n")

    with open(
        full_file_path,
        "w",
        encoding="utf-8"
    ) as f:
        if existing_content:
            content_to_write = (
                existing_content
                + "\n\n"
                + new_entry
                + "\n"
            )
        else:
            content_to_write = new_entry + "\n"
        f.write(content_to_write)
