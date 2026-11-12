import sys
import os
from datetime import datetime


def main() -> None:
    dirs = []
    file_name = None

    # Manual parsing of sys.argv to support -d and -f flags in any order
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "-d":
            i += 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                dirs.append(sys.argv[i])
                i += 1
            continue
        elif arg == "-f":
            i += 1
            if i < len(sys.argv):
                file_name = sys.argv[i]
                i += 1
            continue
        else:
            i += 1

    # 1. Handle directory creation if -d is provided
    dir_path = ""
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

    # 2. Handle file creation and content input if -f is provided
    if file_name:
        if dir_path:
            target_file = os.path.join(dir_path, file_name)
        else:
            target_file = file_name

        # Ensure parent directories exist
        parent_dir = os.path.dirname(target_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        # Collect lines interactively until "stop"
        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        # Generate timestamp and format content with numbered lines
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        formatted_entry = [timestamp]
        for idx, content_line in enumerate(lines, 1):
            formatted_entry.append(f"{idx} {content_line}")

        new_content = "\n".join(formatted_entry) + "\n"

        # Append if file already exists, otherwise create new
        mode = "a" if os.path.exists(target_file) else "w"
        with open(target_file, mode, encoding="utf-8") as f:
            f.write(new_content)


if __name__ == "__main__":
    main()
