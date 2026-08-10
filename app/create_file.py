import argparse
import os
from datetime import datetime


def parse_command_line() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        nargs="*",
        type=str,
        default=[""],
    )
    parser.add_argument(
        "-f",
        nargs="?",
        type=str,
    )
    args = parser.parse_args()

    return os.path.join(os.getcwd(), *args.d, args.f or "")


def generate_content() -> list[str]:
    lines = [f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"]
    line_count = 0

    while True:
        content = input("Enter content line: ")

        if content == "stop":
            return lines

        line_count += 1
        lines.append(f"{line_count} {content.strip()}\n")


def create_file() -> None:
    destination = parse_command_line()
    dir_name = os.path.dirname(destination)

    if dir_name:
        try:
            os.makedirs(dir_name)
        except FileExistsError as e:
            print(e)

    if os.path.basename(destination):
        content = generate_content()

        if os.path.exists(destination):
            content.insert(0, "\n")

        with open(destination, "a") as file:
            file.writelines(content)


create_file()
