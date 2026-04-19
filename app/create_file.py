import argparse
from pathlib import Path
import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser(description="Create file")
    parser.add_argument(
        "-d",
        "--directory",
        nargs="*",
        default=".",
        help="Directory to create"
    )
    parser.add_argument("-f", "--file", required=True, help="File to create")
    args = parser.parse_args()

    folder_path = Path(*args.directory)
    full_path = folder_path / args.file

    full_path.parent.mkdir(parents=True, exist_ok=True)

    formated_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [formated_time]
    count = 1
    while True:

        user_input = input("> ")

        if user_input.strip().lower() == "stop":
            break

        content.append(f"{count} {user_input}")
        count += 1

    final_text = "\n".join(content) + "\n\n"
    with open(full_path, "a") as f:
        f.write(final_text)


if __name__ == "__main__":
    create_file()
