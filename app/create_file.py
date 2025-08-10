import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:

    directory_path = None
    filename = None

    if "-d" in args:
        d_index = args.index("-d")
        paths = []
        i = d_index + 1
        while i < len(args) and not args[i].startswith("-"):
            paths.append(args[i])
            i += 1
        if paths:
            directory_path = os.path.join(*paths)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    return directory_path, filename


def get_content() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    line_number = 1

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break

        lines.append(f"{line_number} {line}")
        line_number += 1

    if lines:
        return f"{timestamp}\n" + "\n".join(lines) + "\n"
    return ""


def create_or_update_file(
        directory_path: str | None,
        filename: str | None
) -> None:
    if not any([directory_path, filename]):
        raise ValueError("No directory or file specified")

    if directory_path:
        try:
            os.makedirs(directory_path, exist_ok=True)
            print(f"Created directory: {directory_path}")
        except OSError as e:
            print(f"Error creating directory: {e}")
            return

    if filename:
        full_path = os.path.join(directory_path or "", filename)

        content = get_content()
        if not content:
            return

        try:
            mode = "a" if os.path.exists(full_path) else "w"

            with open(full_path, mode) as file:
                if mode == "a" and os.path.getsize(full_path) > 0:
                    file.write("\n\n")
                file.write(content)

            print(f"Successfully "
                  f"{'updated' if mode == 'a' else 'created'}: "
                  f"{full_path}")

        except OSError as e:
            print(f"Error working with file: {e}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Create directory: python create_file.py -d dir1 dir2")
        print("  Create file: python create_file.py -f file.txt")
        print("  Create both: python create_file.py -d dir1 dir2 -f file.txt")
        return

    try:
        directory_path, filename = parse_args(sys.argv[1:])

        if directory_path is None and filename is None:
            print("Error: No valid flags provided (-d or -f required)")
            return

        create_or_update_file(directory_path, filename)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
