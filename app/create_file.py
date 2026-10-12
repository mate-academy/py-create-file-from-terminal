import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]

    d_index = args.index("-d") if "-d" in args else -1
    f_index = args.index("-f") if "-f" in args else -1

    directories = []
    filename = None

    if d_index != -1 and f_index != -1:
        if d_index < f_index:
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]

    elif d_index != -1:
        directories = args[d_index + 1:]

    if f_index != -1 and f_index + 1 < len(args):
        filename = args[f_index + 1]

    if directories:
        os.makedirs(os.path.join(*directories), exist_ok=True)

    if filename is None:
        return

    filepath = (
        os.path.join(*directories, filename)
        if directories
        else filename
    )

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    if not lines:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n"

    numbered_lines = [
        f"{number} {line}"
        for number, line in enumerate(lines, start=1)
    ]
    content += "\n".join(numbered_lines)
    content += "\n"

    if os.path.exists(filepath):
        content = "\n" + content

    with open(filepath, "a", encoding="utf-8") as file:
        file.write(content)


main()
