import os
import sys
from datetime import datetime


def create_flags_list(argv: list) -> dict:
    # Simplified exception handling
    flags = {}
    try:
        flags["-d"] = argv.index("-d")
        flags["-f"] = argv.index("-f")
    except ValueError:
        pass  # No flags, continue processing

    return flags


def make_dir(*args: list) -> None:
    # Using os.path.join for cross-platform compatibility
    os.makedirs(os.path.join(*args))


def create_file_and_content(filename: str) -> None:
    content_lines = []
    line_number = 1  # Initialize line number
    while True:
        content = input("Enter content line: ")
        if content.lower().strip() == "stop":
            break
        # Add line number before each line of content
        content_lines.append(f"{line_number}. {content}")
        line_number += 1  # Increment line number

    with open(filename, "a") as fn:
        fn.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")  # Write timestamp
        fn.writelines(line + "\n" for line in content_lines)  # Write each numbered line


if __name__ == "__main__":
    argv = list(sys.argv)
    path = ""
    dictionary = create_flags_list(argv=argv)

    if dictionary.get("-d", False):
        # Use os.path.join for path construction
        path = os.path.join(*argv[dictionary["-d"] + 1:dictionary.get("-f", -1)])
        make_dir(path)

    if dictionary.get("-f", False):
        file_name = argv[dictionary["-f"] + 1]
        if path:
            # Use os.path.join for file path construction
            filename = os.path.join(path, file_name)
        else:
            filename = file_name
        print(filename)
        create_file_and_content(filename=filename)
