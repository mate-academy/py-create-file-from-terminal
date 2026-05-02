import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # Collect directory parts until the next flag or end of args
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            continue
        else:
            i += 1

    target_dir = "."
    if dir_parts:
        target_dir = os.path.join(*dir_parts)
        os.makedirs(target_dir, exist_ok=True)

    if not file_name:
        return

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_block = [timestamp]

    for idx, line in enumerate(content_lines, start=1):
        formatted_block.append(f"{idx} {line}")

    full_content = "\n".join(formatted_block)

    file_path = os.path.join(target_dir, file_name)
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n\n")
        output_file.write(full_content)


if __name__ == "__main__":
    main()
