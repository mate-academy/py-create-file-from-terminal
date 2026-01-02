import os
from datetime import datetime
from argparse import ArgumentParser


def create_file(path: str, file_name: str, content: str) -> None:
    if len(path):
        os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, file_name) if path else file_name

    with open(file_path, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for index, line in enumerate(content.splitlines()):
            file.write(f"{index + 1} {line}\n")


def main() -> None:
    content = ""
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        action="store",
        type=str,
        nargs="*"
    )
    parser.add_argument("-f", "--file", help="Create file")

    args = parser.parse_args()

    if args.file:
        user_answers = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            user_answers.append(line)
        content = "\n".join(user_answers)

    if args.directory:
        create_file("/".join(args.directory), args.file, content)
    else:
        create_file("", args.file, content)


if __name__ == "__main__":
    main()
