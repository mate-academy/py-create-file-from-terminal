import argparse
import os
from datetime import datetime


def create_dirs(dir_1: str, dir_2: str) -> None:
    os.makedirs(os.path.join(os.getcwd(), dir_1, dir_2), exist_ok=True)


def get_user_input() -> str:
    lines = []
    line_index = 0
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        line_index += 1
        lines.append(f"{line_index} {line}")
    return "\n".join(lines)


def write_content_to_file(file_name: str, content: str) -> None:
    try:
        with open(file_name, "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(content)
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and fill a file with content"
    )
    parser.add_argument("-d",
                        "--dir",
                        nargs=2,
                        help="Directory names",
                        metavar=("dir_1", "dir_2"))

    parser.add_argument("-f",
                        "--file",
                        help="File name")

    args = parser.parse_args()

    if args.dir:
        create_dirs(args.dir[0], args.dir[1])
        if args.file:
            file_path = os.path.join(os.getcwd(),
                                     args.dir[0],
                                     args.dir[1],
                                     args.file)
            content = get_user_input()
            write_content_to_file(file_path, content)
    elif args.file:
        content = get_user_input()
        write_content_to_file(args.file, content)


if __name__ == "__main__":
    main()
