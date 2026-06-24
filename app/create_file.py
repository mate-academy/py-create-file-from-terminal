import os
import sys
from datetime import datetime
from typing import List


def parse_arguments() -> tuple[List[str], str | None]:
    args = sys.argv[1:]
    directory_path = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            if f_index > d_index:
                directory_path = args[d_index + 1:f_index]
                file_name = args[f_index + 1] if (f_index + 1
                                                  < len(args)) else None
        else:
            directory_path = args[d_index + 1:]
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1] if f_index + 1 < len(args) else None

    return directory_path, file_name


def create_directory(path_parts: List[str]) -> str:
    if not path_parts:
        return os.getcwd()
    full_path = os.path.join(os.getcwd(), *path_parts)
    os.makedirs(full_path, exist_ok=True)
    return full_path


def get_user_content() -> List[str]:
    print("Enter content lines (type 'stop' to finish):")
    lines = []
    while True:
        line = input("Enter content line: ").strip()
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: List[str]) -> List[str]:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [timestamp] + [f"{i + 1} {line}" for i, line in enumerate(lines)]


def write_to_file(file_path: str, content: List[str]) -> None:
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        content = [""] + content
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n")


def main() -> None:
    directory_path, file_name = parse_arguments()
    full_path = create_directory(directory_path)

    if file_name:
        file_path = os.path.join(full_path, file_name)
        user_lines = get_user_content()
        formatted_content = format_content(user_lines)
        write_to_file(file_path, formatted_content)
        print(f"File '{file_name}' created or updated at '{file_path}'.")
    else:
        print(f"Directory created at '{full_path}'.")


if __name__ == "__main__":
    main()
