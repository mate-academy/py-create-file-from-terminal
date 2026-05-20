import os
import sys
from datetime import datetime


def parse_arguments() -> tuple[list[str], str | None]:
    args = sys.argv[1:]
    args_len = len(args)
    dirs = list()
    file_name = None

    idx = 0
    while idx < args_len:
        if args[idx] == "-d":
            idx += 1
            while idx < args_len and not args[idx].startswith("-"):
                dirs.append(args[idx])
                idx += 1
        elif args[idx] == "-f":
            idx += 1
            if idx < args_len:
                file_name = args[idx]
                idx += 1
        else:
            idx += 1

    return dirs, file_name


def collect_file_contents() -> list[str]:
    file_contents = list()

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        file_contents.append(line)

    return file_contents


def write_to_file(file_path: str, file_contents: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_contents = [f"{i + 1} {line}"
                         for i, line in enumerate(file_contents)]
    contents_block = ("\n" + timestamp + "\n"
                      + "\n".join(numbered_contents) + "\n")

    with open(file_path, "a") as f:
        f.write(contents_block)


def main() -> None:
    dirs, file_name = parse_arguments()

    if not dirs and not file_name:
        print("Usage: create_file.py [-d dir1 [dir2 ...]] [-f file_name]")
        return

    base_path = os.getcwd()

    if dirs:
        dir_path = os.path.join(base_path, *dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = base_path

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        file_contents = collect_file_contents()
        write_to_file(file_path, file_contents)


if __name__ == "__main__":
    main()
