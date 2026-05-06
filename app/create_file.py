import sys
import os
from datetime import datetime


def create_app() -> None:
    args = sys.argv[1:]

    dirs = []
    filename = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    full_path = ""
    if dirs:
        full_path = os.path.join(*dirs)
        os.makedirs(full_path, exist_ok=True)
    if filename:
        if full_path:
            final_path = os.path.join(full_path, filename)
        else:
            final_path = filename

        lines = []
        while True:
            try:
                line_content = input("Enter content line: ")
                if line_content.strip() == "stop":
                    break
                lines.append(line_content)
            except StopIteration:
                break

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if os.path.exists(final_path):
            with open(final_path, "a") as f:
                f.write("\n")

        with open(final_path, "a") as f:
            f.write(f"{current_time}\n")
            for num, line in enumerate(lines, start=1):
                f.write(f"{num} {line}\n")


create_app()
