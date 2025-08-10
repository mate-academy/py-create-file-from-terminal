import sys
import os
from datetime import datetime


def create_file_with_content(filepath: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = [
        f"{i + 1}{line}" for i, line in enumerate(content_lines)]
    content_to_write = [timestamp] + numbered_content

    try:
        with open(filepath, "a") as f:
            for line in content_to_write:
                f.write(line + "\n")
        print(f"File '{filepath}' created/updated successfully.")
    except Exception as e:
        print(f"Error writing to file '{filepath}': {e}")


if __name__ == "__main__":
    args = sys.argv[1:]
    dir_path_parts = []
    file_name = None
    create_directory = False
    create_file = False

    i = 0
    while i < len(args):
        if args[i] == "-d":
            create_directory = True
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_path_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            create_file = True
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                print("Error: File name not specified after -f flag.")
                sys.exit(1)
        else:
            print(f"Unknown flag or argument: {args[i]}")
            sys.exit(1)

    if create_directory and dir_path_parts:
        directory_path = os.path.join(*dir_path_parts)
        try:
            os.makedirs(directory_path, exist_ok=True)
            print(f"Directory '{directory_path}' created successfully.")
        except Exception as e:
            print(f"Error creating directory '{directory_path}': {e}")
            sys.exit(1)
    elif create_directory and not dir_path_parts:
        print("Warning: -d flag passed without specifying directory path.")

    if create_file and file_name:
        if create_directory and dir_path_parts:
            filepath = os.path.join(directory_path, file_name)
        else:
            filepath = file_name

        print("Enter content lines (type 'stop' to finish):")
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            content_lines.append(line)

        if content_lines:
            create_file_with_content(filepath, content_lines)
        else:
            print("No content entered, file not created/updated.")
    elif create_file and not file_name:
        print("Error: -f flag passed without specifying file name.")
