import sys
import os
from datetime import datetime
from typing import List, Optional


def create_directory(path: str) -> None:
    """Creates a directory at the specified path."""
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")


def create_file(file_path: str) -> None:
    """Creates or appends content to a file at the specified path."""
    lines: List[str] = []
    while True:
        line: str = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content: str = (f"{timestamp}\n"
                    + "\n".join(f"{i + 1} {line}"
                                for i, line in enumerate(lines)))

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n\n" + content)
    else:
        with open(file_path, "w") as file:
            file.write(content)

    print(f"File '{file_path}' created/updated successfully.")


def main() -> None:
    """Main function to handle command-line arguments
     and create directories or files."""
    args: List[str] = sys.argv[1:]

    path: Optional[str] = None
    file_name: Optional[str] = None

    # Handle directory creation if -d flag is present
    if "-d" in args:
        d_index: int = args.index("-d")
        if "-f" in args:
            f_index: int = args.index("-f")
            if d_index < f_index:
                # Extract path components between -d and -f
                path_components: List[str] = args[d_index + 1:f_index]
                path = os.path.join(*path_components)
                file_name = args[f_index + 1]
            else:
                # Extract path components after -d
                path_components = args[d_index + 1:]
                path = os.path.join(*path_components)
        else:
            # Extract path components after -d
            path_components = args[d_index + 1:]
            path = os.path.join(*path_components)
        create_directory(path)

    # Handle file creation if -f flag is present
    if "-f" in args:
        f_index = args.index("-f")
        if path:
            # If path is defined, create file within the path
            if file_name is None:
                file_name = args[f_index + 1]
            file_path: str = os.path.join(path, file_name)
        else:
            # If no directory path, create file in current directory
            file_name = args[f_index + 1]
            file_path = file_name
        create_file(file_path)


if __name__ == "__main__":
    main()
