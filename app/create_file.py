import argparse
import datetime
import os

parser = argparse.ArgumentParser(
    prog="python create_file.py",
    description="Program creates directories and file",
)

parser.add_argument("-f", "--file")
parser.add_argument("-d", "--dir", nargs="*")


def handle_dir(dir_path: list[str]) -> None:
    directory_path = os.path.join("", *dir_path)
    os.makedirs(directory_path)


def handle_file(dir_path: list[str] | None, file_name: str) -> None:
    now = datetime.datetime.now()

    file_path = os.path.join(*(dir_path or [""]), file_name)
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n\n")

        file.write(now.strftime("%Y-%m-%d %H:%M:%S\n"))

        line = 1
        lines: list[str] = []

        while True:
            user_input = input("Enter content line: ")

            if user_input == "stop":
                break

            lines.append(f"{line} {user_input}")
            line += 1

        file.write("\n".join(lines))


def main() -> None:
    args = parser.parse_args()

    if not args.file and not args.dir:
        parser.print_help()
        return

    if args.dir:
        handle_dir(dir_path=args.dir)

    if args.file:
        handle_file(dir_path=args.dir, file_name=args.file)


if __name__ == "__main__":
    main()
