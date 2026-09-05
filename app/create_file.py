from datetime import datetime
import os
import sys


def main() -> None:
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

    dir_path = os.path.join(*dirs) if dirs else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if filename:
        file_path = os.path.join(dir_path, filename) if dir_path else filename

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry_lines = [timestamp]
        for idx, line in enumerate(lines, start=1):
            entry_lines.append(f"{idx} {line}")

        entry_content = "\n".join(entry_lines) + "\n"

        file_exists = (os.path.exists(file_path)
                       and os.path.getsize(file_path) > 0)

        with open(file_path, "a") as f:
            if file_exists:
                f.write("\n" + entry_content)
            else:
                f.write(entry_content)


if __name__ == "__main__":
    main()
else:
    main()
