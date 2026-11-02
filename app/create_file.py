from datetime import datetime
import os
import sys


def parse_args() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    directories = []
    filename = None
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args) and not args[i].startswith("-"):
                filename = args[i]
                i += 1
        else:
            i += 1
    return directories, filename


def main() -> None:
    directories, filename = parse_args()
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""
    if not filename:
        return
    if dir_path:
        file_path = os.path.join(dir_path, filename)
    else:
        file_path = filename
    lines = []
    line_num = 1
    while True:
        try:
            user_input = input("Enter content line: ")
        except EOFError:
            break
        if user_input.lower() == "stop":
            break
        lines.append(f"{line_num} {user_input}")
        line_num += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", encoding="utf-8") as f:
        if file_exists:
            f.write("\n")
        f.write(timestamp + "\n")
        if lines:
            f.write("\n".join(lines) + "\n")


main()
