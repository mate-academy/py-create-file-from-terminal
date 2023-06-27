import argparse
import os

from datetime import datetime


def create_directory(dirs_list: str) -> None:
    path = os.path.join(*dirs_list)
    os.makedirs(path, exist_ok=True)


def create_content() -> list[str]:
    content = []
    while True:
        content_line = input("Enter content line:")
        if content_line == "stop":
            break
        content.append(content_line + "\n")
    return content


def write_into_file(file_name: str,
                    content: list[str],
                    dirs_list: list[str]) -> None:
    if not dirs_list:
        path = ""
    else:
        path = os.path.join(*dirs_list)
    with open(os.path.join(path, file_name), "a") as new_file:
        new_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for line in content:
            new_file.write(line)


def create_file_inside_directory() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="path", nargs="*", type=str)
    parser.add_argument("-f", dest="file_name")
    args = parser.parse_args()
    if args.path:
        create_directory(args.path)
    if args.file_name:
        content = create_content()
        write_into_file(args.file_name, content, args.path)


if __name__ == "__main__":
    create_file_inside_directory()
