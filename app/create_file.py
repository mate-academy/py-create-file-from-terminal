import datetime
import os
import sys


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    directories: list[str] = []
    filename: str | None = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    return directories, filename


def collect_lines() -> list[str]:
    lines = []
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        lines.append(content)
    return lines


def format_content(lines: list[str]) -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_content = timestamp + "\n"

    for index, line in enumerate(lines, 1):
        formatted_content += f"{index} {line}\n"

    return formatted_content


def write_file(dir_path: str, filename: str, content: str) -> None:
    file_path = os.path.join(dir_path, filename) if dir_path else filename

    if os.path.exists(file_path):
        content = "\n" + content

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)


def main() -> None:
    args = sys.argv[1:]
    directories, filename = parse_args(args)

    dir_path: str = ""
    if directories:
        dir_path = os.path.join(*directories)  # type: ignore
        os.makedirs(dir_path, exist_ok=True)

    if filename is not None:
        lines = collect_lines()
        content = format_content(lines)
        write_file(dir_path, filename, content)


if __name__ in ("__main__", "<run_path>"):
    main()
