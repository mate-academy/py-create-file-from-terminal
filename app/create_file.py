from datetime import datetime
import os
import argparse


def create_file(file_path: str, content: list[str]) -> None:
    with open(file_path, "a") as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def get_file_content() -> list[str]:
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            content.append("")
            break
        content.append(line)
    return content


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="*")
    parser.add_argument("-f", "--file")

    args = parser.parse_args()

    if args.directory:
        directory_path = args.directory
        if args.file:
            file_name = args.file
            os.makedirs(os.path.join(*directory_path), exist_ok=True)
            file_path = os.path.join(*directory_path, file_name)
            content = get_file_content()
            create_file(file_path, content)
        else:
            os.makedirs(os.path.join(*directory_path), exist_ok=True)
    elif args.file:
        file_name = args.file
        content = get_file_content()
        create_file(file_name, content)


if __name__ == "__main__":
    main()
