import os
import sys
from datetime import datetime

USAGE = (
    "Usage:\n"
    "  python create_file.py -d dir1 dir2 [...]\n"
    "  python create_file.py -f file.txt\n"
    "  python create_file.py -d dir1 dir2 -f file.txt"
)


def parse_args(argv: list[str]) -> tuple[list[str], str | None]:
    dirs: list[str] = []
    file_name: str | None = None
    current: str | None = None  # flag we are currently collecting values for

    for arg in argv:
        if arg in ("-d", "-f"):
            current = arg
            continue
        if current == "-d":
            dirs.append(arg)
        elif current == "-f":
            if file_name is None:
                file_name = arg
            else:
                raise ValueError("Only one file name is allowed after -f.")
        else:
            raise ValueError(f"Unexpected argument: {arg}")

    return dirs, file_name


def read_content() -> list[str]:
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_content(path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = [timestamp]
    block += [f"{number} {line}" for number, line in enumerate(lines, 1)]

    has_content = os.path.exists(path) and os.path.getsize(path) > 0
    with open(path, "a", encoding="utf-8") as output_file:
        if has_content:
            output_file.write("\n")  # blank line between blocks
        output_file.write("\n".join(block) + "\n")


def main() -> None:
    argv = sys.argv[1:]
    if not argv:
        print(USAGE)
        sys.exit(1)

    try:
        dirs, file_name = parse_args(argv)
    except ValueError as err:
        print(f"Error: {err}\n{USAGE}")
        sys.exit(1)

    if "-d" in argv and not dirs:
        print(f"Error: -d requires at least one directory name.\n{USAGE}")
        sys.exit(1)
    if "-f" in argv and file_name is None:
        print(f"Error: -f requires a file name.\n{USAGE}")
        sys.exit(1)

    target_dir = os.path.join(*dirs) if dirs else os.getcwd()
    if dirs:
        os.makedirs(target_dir, exist_ok=True)
        print(f"Directory ready: {target_dir}")

    if file_name:
        lines = read_content()
        path = os.path.join(target_dir, file_name)
        write_content(path, lines)
        print(f"Content written to: {path}")


if __name__ in ("__main__", "<run_path>"):
    main()
