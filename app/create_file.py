import sys
import os
import datetime


def create_file(parts_directory: list[str],
                file_name: str,
                file_content: list[str]
                ) -> None:
    if parts_directory:
        base = os.getcwd()
        dir_path = os.path.join(base, *parts_directory)
        os.makedirs(dir_path, exist_ok=True)
        filepath = os.path.join(dir_path, file_name)
    else:
        filepath = file_name

    file_exists = os.path.exists(filepath)
    file_has_content = file_exists and os.path.getsize(filepath) > 0

    if not file_content:
        return

    mode = "a"
    with (open(filepath, mode) as f):
        if file_has_content:
            f.write("\n")
        timestamp = datetime.datetime.now(
        ).strftime("%Y-%m-%d %H:%M:%S") + "\n"
        f.write(timestamp)
        for i, line in enumerate(file_content, 1):
            f.write(f"{i} {line}\n")


if __name__ == "__main__":
    args = sys.argv[1:]
    directory = []
    filename = None
    mode = None
    i = 0

    while i < len(args):
        arg = args[i]
        if arg == "-d":
            mode = "dir"
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directory.append(args[i])
                i += 1
        elif arg == "-f":
            mode = "file"
            i += 1
            if i >= len(args) or args[i].startswith("-"):
                sys.exit(1)
            filename = args[i]
            i += 1
            if i < len(args):
                sys.exit(1)
        else:
            sys.exit(1)

    if not filename:
        sys.exit(1)

    if os.path.sep in filename:
        sys.exit(1)

    content = []
    try:
        while True:
            line = input("Enter content line: ").strip()
            if line.lower() == "stop":
                break
            content.append(line)
    except EOFError:
        pass

    create_file(parts_directory=directory,
                file_name=filename,
                file_content=content)
