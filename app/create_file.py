import os.path
import sys
from datetime import datetime


def create_file() -> None:
    modes, path = parse_arguments(sys.argv[1:])

    if "-d" in modes:
        _create_dir(modes, path)

    if "-f" in modes:
        text = get_text_from_user()

        try:
            _write_text_to_file(path, text)
        except FileNotFoundError:
            print("File not found")


def parse_arguments(args: list) -> tuple:
    modes = []

    for symbol in ["-d", "-f"]:
        if symbol in args:
            modes.append(symbol)
            args.remove(symbol)

    return modes, os.path.join(*args)


def _create_dir(modes: list, path: str) -> None:
    directory = os.path.dirname(path) if "-f" in modes else path
    os.makedirs(directory, exist_ok=True)


def get_text_from_user() -> str:
    count = 1
    text = ""

    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        text += f"{count} {content}\n"
        count += 1

    return text + "\n"


def _write_text_to_file(path: str, text: str) -> None:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as file:
        file.write(current_date + "\n")
        file.write(text)
