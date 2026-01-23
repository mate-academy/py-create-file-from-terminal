import os
import sys
from datetime import datetime
from typing import List, Optional


def create_directory(path_parts: List[str]) -> str:
    """Create directories from path parts if they don't exist."""
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory created: {directory_path}")
    return directory_path


def create_file(file_path: str, content_source: Optional[str] = None) -> None:
    """Create a file and append content with timestamp and line numbering."""
    with open(file_path, "a") as file:
        # Write timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1

        if content_source:
            # If content_source is provided, read from the file
            with open(content_source, "r") as content_file:
                for line in content_file:
                    file.write(f"{line_number} {line.strip()}\n")
                    line_number += 1
        else:
            # Otherwise, read interactively from the user
            while True:
                content = input("Enter content line: ")
                if content.lower() == "stop":
                    break
                file.write(f"{line_number} {content}\n")
                line_number += 1

    print(f"File created/updated: {file_path}")


def main() -> None:
    args = sys.argv[1:]
    directory_path = ""

    if "-d" in args:
        dir_index = args.index("-d")
        path_parts = []
        for i in range(dir_index + 1, len(args)):
            if args[i] == "-f" or args[i] == "-c":
                break
            path_parts.append(args[i])

        if path_parts:
            directory_path = create_directory(path_parts)
        else:
            print("Error: No directory path provided after -d flag.")
            return

    if "-f" in args:
        file_index = args.index("-f")
        if (file_index + 1 < len(args)
                and args[file_index + 1] not in ["-d", "-c"]):
            file_name = args[file_index + 1]
            file_path = os.path.join(directory_path, file_name)
        else:
            print("Error: No file name provided after -f flag.")
            return
    else:
        print("Error: No file flag (-f) provided.")
        return

    content_source = None
    if "-c" in args:
        content_index = args.index("-c")
        if content_index + 1 < len(args):
            content_source = args[content_index + 1]
        else:
            print("Error: No content source provided after -c flag.")
            return

    create_file(file_path, content_source)


if __name__ == "__main__":
    main()
