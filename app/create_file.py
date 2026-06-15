import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    d_index = args.index("-d") if "-d" in args else None
    f_index = args.index("-f") if "-f" in args else None

    dir_parts = []
    if d_index is not None:
        start = d_index + 1
        end = len(args)
        if f_index is not None and f_index > d_index:
            end = f_index
        dir_parts = args[start:end]

    directory = os.path.join(*dir_parts) if dir_parts else ""
    if directory:
        os.makedirs(directory, exist_ok=True)

    if f_index is None:
        return

    filename = "file.txt"
    if f_index + 1 < len(args):
        if args[f_index + 1] != "-d":
            filename = args[f_index + 1]
        elif f_index > 0 and args[f_index - 1] != "-d":
            filename = args[f_index - 1]

    full_path = os.path.join(directory, filename) if directory else filename

    lines = []
    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        lines.append(text)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [f"{i + 1} {line}\n" for i, line in enumerate(lines)]

    content = timestamp + "\n" + "".join(formatted_lines)

    file_exists = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    with open(full_path, "a", encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n")
        output_file.write(content)


main()
