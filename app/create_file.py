import os
import sys
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

    return path


def main() -> None:
    args = sys.argv[1:]
    i = 0
    dirs = []
    file_name = None

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            # Invalid argument, skip or handle error
            i += 1

    path = None
    if dirs:
        path = create_path(dirs)

    if file_name:
        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        content = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        for idx, line in enumerate(lines, 1):
            content.append(f"{idx} {line}")

        full_file_path = os.path.join(path, file_name) if path else file_name

        with open(full_file_path, "a") as f:
            if os.path.exists(full_file_path) and \
                    os.path.getsize(full_file_path) > 0:
                f.write("\n")
            f.write("\n".join(content) + "\n")


if __name__ in ("__main__", "<run_path>"):
    main()
