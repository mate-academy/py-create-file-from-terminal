import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def parse_arguments() -> tuple:
    args = sys.argv[1:]

    directories = []
    filename = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]
        else:
            print("Error: File name not provided.")
            sys.exit(1)

    return directories, filename


def create_directories(directories: list) -> str:
    if directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def det_content_from_user() -> list:
    lines = []
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter}. {line}")
        counter += 1

    return lines


def write_to_file(path: str, filename: str, content_lines: list) -> None:
    file_path = os.path.join(path, filename) if path else filename

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        file.write(get_timestamp() + "\n")
        for line in content_lines:
            file.write(line + "\n")

    print(f"\nFile created/updated at: {file_path}")


def main() -> None:
    directories, filename = parse_arguments()

    if not filename and not directories:
        print("Error: No flags provided. Use -d and/or -f.")
        sys.exit(1)

    path = create_directories(directories)

    if filename:
        content_lines = det_content_from_user()
        write_to_file(path, filename, content_lines)

    if __name__ == "__main__":
        main()
