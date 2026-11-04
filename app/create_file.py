import os
import sys
from datetime import datetime

def create_file() -> None:
    args = sys.argv[1:]
    dirs = []
    file_name = None
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    target_dir = ""
    if dirs:
        target_dir = os.path.join(*dirs)
        os.makedirs(target_dir, exist_ok=True)

    if not file_name:
        return

    full_path = (
        os.path.join(target_dir, file_name)
        if target_dir
        else file_name
    )

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_parts = [timestamp]
    for index, text in enumerate(lines, start=1):
        content_parts.append(f"{index} {text}")
    new_content = "\n".join(content_parts) + "\n"

    file_exists = os.path.exists(full_path)
    mode = "a" if file_exists else "w"
    with open(full_path, mode, encoding="utf-8") as f:
        if file_exists:
            f.write("\n")
        f.write(new_content)

# IMPORTANT: no `if __name__ == "__main__"` – the tests use runpy without run_name="__main__"
create_file()
