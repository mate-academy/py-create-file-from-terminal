import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    """
        Returns the current date and time as a formatted string.
        Returns:
            str: Current date and time in "YYYY-MM-DD HH:MM:SS" format
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_directory(path_parts: list) -> str:
    """
        Creates directories based on the provided path parts.
        Args:
            path_parts (list): List of directory names.
        Returns:
            str: The full path of the created directory.
    """
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def collect_file_content() -> list:
    """
        Collects lines of content from user input until 'stop' is entered.
        Returns:
            list: List of content lines.
    """
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break

        lines.append(user_input)

    return lines


def format_content(lines: list) -> str:
    """
        Formats the content with a timestamp and line numbers.
        Args:
            lines (list): List of content lines.
        Returns:
            str: Formatted content string.
    """
    timestamp = get_timestamp()
    numbered = [f"{i} {line}" for i, line in enumerate(lines, 1)]

    return "\n".join([timestamp] + numbered) + "\n"


def write_to_file(file_path: str, content: str) -> None:
    """
        Writes content to a file, appending if the file already exists.
        Args:
            file_path (str): Path to the file.
            content (str): Content to write.
    """
    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(content)


def parse_arguments(args: list) -> tuple:
    """
        Parses command-line arguments to extract directories and filename.
        Args:
            args (list): List of command-line arguments.
        Returns:
            tuple: (list of directories, filename)
    """
    directories = []
    filename = None
    mode = None

    for arg in args:
        if arg == "-d":
            mode = "dir"
            continue
        if arg == "-f":
            mode = "file"
            continue

        if mode == "dir":
            directories.append(arg)
        elif mode == "file" and not filename:
            filename = arg

    return directories, filename


def main() -> None:
    """Main function to execute the file creation process."""
    directories, filename = parse_arguments(sys.argv[1:])

    base_path = ""
    if directories:
        base_path = create_directory(directories)

    if filename:
        filepath = os.path.join(base_path, filename) if base_path else filename

        lines = collect_file_content()
        if lines:
            content = format_content(lines)
            write_to_file(filepath, content)


if __name__ == "__main__":
    main()
