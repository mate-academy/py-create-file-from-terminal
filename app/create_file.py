import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    dirs = []
    filename = None
    if "-d" in args:
        d_index = args.index("-d") + 1
        for i in range(d_index, len(args)):
            if args[i].startswith("-"):
                break
            dirs.append(args[i])
    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            filename = args[f_index]
        else:
            print("Error: filename must be provided after -f")
            exit(1)  # или sys.exit(1)
        f_index = args.index("-f") + 1
        if f_index < len(args):
            filename = args[f_index]
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
    else:
        path = "."
    lines = []
    if filename:
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            lines.append(line)
        full_path = os.path.join(path, filename)
        if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
            prepend_newline = True
        else:
            prepend_newline = False

        with open(full_path, "a") as f:
            if prepend_newline:
                f.write("\n")  # разделяем старый и новый блок
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            for i, line in enumerate(lines, start=1):
                f.write(f"{i} {line}\n")


if __name__ == "__main__":
    create_file()
