import argparse

import os

from datetime import datetime

from typing import List


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create -d and -f and write content inside them."
    )
    parser.add_argument("-d", nargs="+", help="Create directories.")
    parser.add_argument("-f", help="Create a file.")

    args = parser.parse_args()

    if args.d:
        create_directories(args.d)

    if args.f:
        create_file(args.f)


def create_directories(dirs: List[str]) -> None:
    path = os.path.join(*dirs)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
    except FileExistsError:
        print(f"Directory already exists: {path}")


def collect_input_lines() -> List[str]:
    print("Enter content line (type 'stop' to finish):")
    content = []
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)
    return content


def create_file(filename: str) -> None:
    content = collect_input_lines()

    mode = "w" if not os.path.exists(filename) else "a"
    with open(filename, mode) as file:
        if mode == "a":
            file.write("\n\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        content = [f"{i + 1} {line}" for i, line in enumerate(content)]
        file.write("\n".join(content))

    print(f"File created/updated: {filename}")


if __name__ == "__main__":
    main()
