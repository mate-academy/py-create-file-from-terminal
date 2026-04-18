import os
import sys
from datetime import datetime


def get_file_content() -> list:
    """
    Collects lines of content from the user until 'stop' is entered.
    """
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(file_path: str, content: list) -> None:
    """
    Writes a timestamp and numbered lines to the specified file.
    Appends if the file already exists.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as output_file:
        output_file.write(f"{timestamp}\n")
        for index, line in enumerate(content, start=1):
            output_file.write(f"{index} {line}\n")
        output_file.write("\n")


def main() -> None:
    """
    Parses sys.argv to create directories and files based on flags.
    """
    args = sys.argv[1:]
    dir_parts = []
    file_name = ""

    # Parsing flags and arguments
    if "-d" in args:
        d_index = args.index("-d")
        # Collect items until the next flag or end of list
        for item in args[d_index + 1:]:
            if item == "-f":
                break
            dir_parts.append(item)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    # Create directory path if -d was provided
    current_path = os.getcwd()
    if dir_parts:
        path_to_create = os.path.join(current_path, *dir_parts)
        os.makedirs(path_to_create, exist_ok=True)
        current_path = path_to_create

    # Process file creation if -f was provided
    if file_name:
        file_path = os.path.join(current_path, file_name)
        content = get_file_content()
        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
