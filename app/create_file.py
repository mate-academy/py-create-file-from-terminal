from datetime import datetime
import os
import argparse


def create_file(path: list[str], filename: str) -> None:
    os.makedirs(os.path.join(os.getcwd(), *path), exist_ok=True)
    with open(os.path.join(os.getcwd(), *path, filename), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content == "stop":
                break
            file.write(f"{count} {line_content}\n")
            count += 1
        file.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        "--dirname",
        nargs="+",
        type=str,
        help="Path to the file"
    )
    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        help="Name of the file"
    )
    args = parser.parse_args()

    if args.dirname or args.filename:
        create_file(
            args.dirname,
            args.filename[0] if args.filename else "file.txt"
        )


if __name__ == "__main__":
    main()
