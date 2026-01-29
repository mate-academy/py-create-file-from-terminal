import os
from datetime import datetime
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a directory and/or file with user input.")
    parser.add_argument('-d', '--directory', nargs='+', help='Specify the directory path.', default=[])
    parser.add_argument('-f', '--file', help='Specify the file name.')
    return parser.parse_args()


def create_directory(path_list: list[str]) -> str:
    directory_path = os.path.join(*path_list)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def collect_user_input() -> list[str]:
    lines = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"\n{current_time}\n")

    line_count = 1
    while True:
        line = input("Enter content line (type 'stop' to finish): ")
        if line.lower() == "stop":
            break
        lines.append(f"{line_count} {line}\n")
        line_count += 1

    return lines


def create_file(file_path: str, content: list[str]) -> None:
    with open(file_path, "a") as file:
        file.writelines(content)


def main() -> None:
    args = parse_args()

    if args.directory:
        directory_path = create_directory(args.directory)
        if args.file:
            file_path = os.path.join(directory_path, args.file)
            content = collect_user_input()
            create_file(file_path, content)
    elif args.file:
        content = collect_user_input()
        create_file(args.file, content)
    else:
        raise ValueError(
            "Invalid arguments."
            " Use -d to specify directory or -f to specify file name."
        )


if __name__ == "__main__":
    main()
