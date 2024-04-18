import os
import argparse
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(filename: str, content: list[str]) -> None:
    try:
        with open(filename, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp + "\n")
            for idx, line in enumerate(content, start=1):
                file.write(f"{idx} {line}\n")
            file.write("\n")
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")


def writing_content() -> list[str]:
    content = []
    while True:
        line = input("Enter contenr line: ")
        if line.lower() == "stop":
            break
        content.append(line)
    return content


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directory and file with content")
    parser.add_argument("-d", "--directory",
                        help="Directory path", required=True)
    parser.add_argument("-f", "--filename",
                        help="File name", required=True)
    args = parser.parse_args()
    directory_path = args.directory
    filename = args.filename
    create_directory(directory_path)

    content = writing_content()
    content_list = [f"{line}\n" for line in content]

    create_file(os.path.join(directory_path, filename), content_list)


if __name__ == "__main__":
    main()
