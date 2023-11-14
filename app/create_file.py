import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str, content_lines: str) -> None:
    # Create directory if it doesn't exist
    if directory:
        dir_path = os.path.join(*directory)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    file_path = os.path.join(dir_path, filename)

    # Add timestamp and line numbers
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [f"{i + 1} {line}" for i, line in enumerate(content_lines)]

    # Read existing content if file already exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_content = file.read().strip().split("\n")
        content = existing_content + ["", timestamp] + content

    # Write content to file
    with open(file_path, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    # Parse command line arguments
    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = sys.argv[directory_index:]
        filename = None
    elif "-f" in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        directory = []
        filename = sys.argv[filename_index]
    else:
        print("Please provide either -d or -f flag.")
        sys.exit(1)

    # Read content lines from the user
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Call the create_file function with the provided arguments
    create_file(directory, filename, content_lines)

    print("File created successfully.")
