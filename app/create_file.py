import argparse
import os


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create directories and files from the terminal."
    )
    parser.add_argument(
        "-d",
        nargs="+",
        metavar="DIR",
        help="List of directory names that form a nested path "
             "(e.g. -d dir1 dir2 -> dir1/dir2).",
    )
    parser.add_argument(
        "-f",
        metavar="FILENAME",
        help="Name of the file to create.",
    )
    return parser.parse_args()


def build_directory_path(dirs: list[str]) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def read_content_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def create_file(directory: str | None, filename: str) -> None:
    full_path = os.path.join(directory, filename) if directory else filename

    lines = read_content_lines()

    with open(full_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"File '{full_path}' created successfully.")


def main() -> None:
    args = parse_args()

    if not args.d and not args.f:
        print("You must provide at least one flag: -d or -f.")
        return

    directory = None

    if args.d:
        directory = build_directory_path(args.d)
        if not args.f:
            print(f"Directory '{directory}' created successfully.")

    if args.f:
        create_file(directory, args.f)


if __name__ == "__main__":
    main()