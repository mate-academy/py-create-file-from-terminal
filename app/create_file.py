import argparse
from pathlib import Path
import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser(description="Create file")
    parser.add_argument(
        "-d",
        "--directory",
        nargs="*",
        default=[],
        help="Directory to create"
    )
    parser.add_argument("-f", "--file", help="File to create")
    args = parser.parse_args()

    folder_path = Path(*args.directory)

    folder_path.mkdir(parents=True, exist_ok=True)

    if args.file:
        full_path = folder_path / args.file
        full_path.parent.mkdir(parents=True, exist_ok=True)
        formatted_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = [formatted_time]
        count = 1
        while True:

            user_input = input("Enter content line: ")

            if user_input.strip().lower() == "stop":
                break

            content.append(f"{count} {user_input}")
            count += 1

        final_text = "\n".join(content) + "\n\n"
        with open(full_path, "a") as file:
            file.write(final_text)


if __name__ == "__main__":
    create_file()
