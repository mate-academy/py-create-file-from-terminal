import sys
import os
from datetime import datetime


def create_directory(path_parts):
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")
    return path


def create_file(file_path):
    # Get content from user input until 'stop' is entered
    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    # Prepare content with timestamp and numbered lines
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = [f"{i + 1} {line}" for i,
    line in enumerate(content_lines)]

    # Write content to file, append if the file already exists
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(f"{timestamp}\n")
        file.write("\n".join(numbered_content) + "\n")

    print(f"File '{file_path}' created/updated successfully.")


def main():
    args = sys.argv[1:]

    if "-d" in args:
        # Extract path parts after -d flag
        d_index = args.index("-d")
        path_parts = []
        for part in args[d_index + 1:]:
            if part.startswith("-"):
                break
            path_parts.append(part)

        if not path_parts:
            print("Error: Directory path not "
                  "specified after '-d' flag.")
            return

        directory_path = create_directory(path_parts)
    else:
        directory_path = "."

    if "-f" in args:
        # Extract file name after -f flag
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Error: File name not specified "
                  "after '-f' flag.")
            return

        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)
    else:
        if "-d" in args:
            print("Error: Missing '-f' flag for "
                  "file creation.")
        else:
            print("Error: Either '-d' or '-f' flag "
                  "must be specified.")


if __name__ == "__main__":
    main()
