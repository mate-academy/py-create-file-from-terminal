import sys
import os
from datetime import datetime


def create_directory(path_parts: list[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def get_content() -> list[str]:
    content = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)
    return content


def write_to_file(file_path: str, content: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as f:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write(f"{timestamp}\n")
        for i, line in enumerate(content, 1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py -d [directories] -f [filename]")
        return

    dir_path = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path = args[d_index + 1:f_index]
            file_name = args[f_index + 1] if f_index + 1 < len(args) else None
        else:
            dir_path = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1] if f_index + 1 < len(args) else None

    dir_full_path = create_directory(dir_path) if dir_path else os.getcwd()

    if file_name:
        file_path = os.path.join(dir_full_path, file_name)
        content = get_content()
        write_to_file(file_path, content)
        print(f"File updated: {file_path}")
    elif dir_path:
        print(f"Directory created: {dir_full_path}")
    else:
        print("Error: No filename specified.")


if __name__ == "__main__":
    main()
