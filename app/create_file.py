import argparse
import os

from datetime import datetime


def make_dir(command: list) -> None:
    full_path = os.path.join(*command)

    if full_path:
        os.makedirs(full_path, exist_ok=True)


def write_in_file(file_path: str) -> None:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = "\n" if os.path.exists(file_path) else ""

    with open(file_path, "a") as file:
        content += current_date + "\n"

        while True:
            new_line = input("Enter new line of content: ") + "\n"

            if "stop" in new_line:
                break
            else:
                content += new_line

        file.write(content)


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, nargs=1, default=[])
    parser.add_argument("-d", type=str, nargs="*", default=[])
    commands = vars(parser.parse_args())

    if len(commands["d"]):
        make_dir(commands["d"])

    if len(commands["f"]):
        write_in_file(os.path.join(*commands["d"] + commands["f"]))


if __name__ == "__main__":
    create_file()
