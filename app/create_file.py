import sys
import os
from datetime import datetime


def parse_args(args: list[str]) -> tuple[str, str]:

    dir_parts = []

    if "-f" not in args:
        raise Exception("Missing -f flag")

    f_index = args.index("-f")

    if f_index + 1 >= len(args):
        raise Exception("Missing file name after -f")

    if args[f_index + 1].startswith("-"):
        raise Exception("Invalid file name")

    file_name = args[f_index + 1]

    if "-d" in args:
        d_index = args.index("-d")

        for item in args[d_index + 1:]:
            if item.startswith("-"):
                break
            dir_parts.append(item)

        if not dir_parts:
            raise Exception("No directory names provided after -d")

        dir_path = os.path.join(*dir_parts)

    else:
        dir_path = ""

    return dir_path, file_name


def get_full_path(dir_path: str, file_name: str) -> str:
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
        return os.path.join(dir_path, file_name)
    return file_name


def content_input() -> list[str]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp]

    print("Enter content line by line (type 'stop' to finish):")

    lines = []
    while True:
        line = input("Line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    for idx, text in enumerate(lines, start=1):
        content.append(f"{idx} {text}")

    return content


def write_file(dir_path: str, file_name: str) -> None:
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    content = content_input()
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as f:
        if file_exists:
            f.write("\n\n")
        for line in content:
            f.write(line + "\n")

    print(f"File created/updated at: {file_path}")


def main() -> None:
    args = sys.argv
    dir_path, file_name = parse_args(args)
    write_file(dir_path, file_name)


if __name__ == "__main__":
    main()
