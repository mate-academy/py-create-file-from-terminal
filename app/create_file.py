import argparse
import os
from datetime import datetime


def make_directory(directory: list[str]) -> str:
    if directory is None:
        return ""
    cleared_segments = [s for s in directory if s.strip()]
    if cleared_segments:
        path = os.path.join(*cleared_segments)
        os.makedirs(path, exist_ok=True)
    else:
        path = ""

    return path


def write_file(path: str, file_name: str) -> None:
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filepath = os.path.join(path, file_name)

    exist = os.path.exists(filepath) and os.path.getsize(filepath) > 0
    with open(filepath, "a", encoding="utf-8") as f:
        if exist:
            f.write("\n")
        i = 1
        f.write(date + "\n")
        while True:
            line = input("Enter content line: ").strip()
            if line == "":
                continue
            if line.strip().lower() == "stop":
                break
            f.write(f"{i} {line}\n")
            i += 1


def create_file() -> None:
    parser = argparse.ArgumentParser(
        description="Create file from terminal",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-d",
        "--directory",
        nargs="+",
        type=str,
        help="directory names separated by spaces",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="file name",
        required=True,
    )

    args = parser.parse_args()

    path = make_directory(args.directory)
    write_file(path, args.file)


if __name__ == "__main__":
    create_file()
