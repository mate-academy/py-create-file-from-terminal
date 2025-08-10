from _datetime import datetime
import os
import sys


def create_directory(directory_parts: list[str]) -> str:
    """
         Create directory from path components
    :param directory_parts:
         List of directory path components
    :return:
         Absolute path to the  created directory
    """
    if not directory_parts:
        return os.getcwd()

    directory_path = os.path.join(*directory_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_file_content() -> list[str]:
    """
        Get content lines from user until 'stop' is entered
    :return:
        List of content lines entered by user
    """

    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        if (line := input("Enter content line: ")).lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def format_content(content_lines: list[str],
                   existing_content: str | None = None) -> str:
    """
        Format content with timestamp and line numbers.
    :param content_lines:
        List of content lines to format.
    :param existing_content:
        Existing content to append.
    :return:
        Formatted content string with timestamp and line numbers.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    format_content = [timestamp]

    for i, line in enumerate(content_lines, 1):
        format_content.append(f"{i} {line}")

    new_content = "\n".join(format_content)

    if existing_content:
        return f"{existing_content}\n\n{new_content}"
    return new_content


def parce_argument(args: list[str]) -> tuple[list[str]] | str:
    """
       Parce command line arguments
    :param args:
       List of command line arguments
    :return:
       Tuple which contain directory parts and filename
    """
    directory_parts = []
    filename = None

    if "-d" in args:
        d_index = args.index("-d")
        try:
            f_index = args.index("-f")
            directory_parts = args[d_index + 1: f_index]
        except ValueError:
            directory_parts = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    return directory_parts, filename


def main() -> None:
    """
       Main function to handle directory and file creation.
    """
    args = sys.argv[1:]
    directory_parts, filename = parce_argument(args)
    content_lines = []

    # Get content if creating a file
    if filename:
        content_lines = get_file_content()

    # Create directory if needed
    directory_path = os.getcwd()
    if directory_parts:
        directory_path = create_directory(directory_parts)

    # Create file if filename provided
    if filename:
        file_path = os.path.join(directory_path, filename)

        # Read existing content if file exists
        existing_content: str | None = None
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                existing_content = f.read()

        # Format new content
        formatted_content = format_content(content_lines, existing_content)

        # Write to file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(formatted_content)

        print(f"File created/updated at: {file_path}")
    elif directory_parts:
        print(f"Directory created at: {directory_path}")
    else:
        print("No action specified. Use -d for directory or -f for file.")


if __name__ == "__main__":
    main()
