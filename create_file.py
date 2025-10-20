import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    """Returns the current timestamp in a readable format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def collect_content() -> list[str]:
    """Prompts user to enter content lines until 'stop' is entered."""
    content_lines = []
    line_number = 1
    while True:
        user_input = input("Enter content line: ")
        if user_input.strip().lower() == "stop":
            break
        content_lines.append(f"{line_number} {user_input}")
        line_number += 1
    return content_lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    """Appends timestamped and numbered content to the specified file."""
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(get_timestamp() + "\n")
        for line in content_lines:
            file.write(line + "\n")
        file.write("\n")  # Separate entries with a blank line


def create_directory_path(directories: list[str]) -> str:
    """Creates nested directories and returns the full path."""
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    """Parses command-line arguments for directory and file flags."""
    dir_parts = []
    file_name = None
    index = 0

    while index < len(arguments):
        if arguments[index] == "-d":
            index += 1
            while (
                index < len(arguments)
                and not arguments[index].startswith("-")
            ):
                dir_parts.append(arguments[index])
                index += 1
        elif arguments[index] == "-f":
            index += 1
            if index < len(arguments):
                file_name = arguments[index]
                index += 1
        else:
            index += 1

    return dir_parts, file_name


def main() -> None:
    """Main entry point for the script."""
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        return

    directories, file_name = parse_arguments(args)
    directory_path = create_directory_path(directories) if directories else ""

    if file_name:
        full_file_path = (
            os.path.join(directory_path, file_name)
            if directory_path else file_name
        )
        content = collect_content()
        write_to_file(full_file_path, content)
        print(f"✅ File created/updated at: {full_file_path}")
    elif directory_path:
        print(f"✅ Directory created at: {directory_path}")
    else:
        print("⚠️ No valid flags provided.")


if __name__ == "__main__":
    main()
