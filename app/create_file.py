
import os
import sys
from datetime import datetime


def main() -> None:
    directories = []
    filename = None

    args = sys.argv[1:]
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                directories.append(args[i])
                i += 1

        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

    if filename is None:
        return

    file_path = os.path.join(directory_path, filename)

    with open(file_path, "a", encoding="utf-8"):
        pass

    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(timestamp + "\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


if __name__ in ("__main__", "<run_path>"):
    main()
