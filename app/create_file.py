import argparse
import os
from datetime import datetime


def create_path(dirs: list[str]) -> str:
    return os.path.join(*dirs)


def get_user_input() -> list[str]:
    content = []
    while True:
        line = input("Enter your text: ")
        if line.strip().lower() == "stop":
            break
        content.append(line)

    return content


def write_to_file(path: str, content: list[str]) -> None:
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_numbers = [
        f"{index + 1} {line}"
        for index, line in enumerate(content)
    ]
    time_with_content = [time_stamp] + content_with_numbers

    flag = os.path.isfile(path) and os.path.getsize(path) > 0

    with open(path, "a") as file:
        if flag:
            file.write("\n")
        file.write("\n".join(time_with_content) + "\n")


def create_dirs(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and/or file with content"
    )
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()

    if args.d:
        dir_path = create_path(args.d)
        create_dirs(dir_path)
    else:
        dir_path = os.getcwd()

    if args.f:
        file_path = os.path.join(dir_path, args.f)
        content = get_user_input()
        write_to_file(file_path, content)

    if not args.d and not args.f:
        print("No directories or files were given")


if __name__ == "__main__":
    main()
