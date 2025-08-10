import os
import sys
from datetime import datetime


def create_directories(path_parts: str) -> None:
    """Create directories based on the provided path."""
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: str) -> None:
    """Prompt the user to input content and write it to the file."""
    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_content = [f"{timestamp}\n"]
    for idx, line in enumerate(content_lines, start=1):
        new_content.append(f"{idx} {line}\n")

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n")
            file.writelines(new_content)
    else:
        with open(file_path, "w") as file:
            file.writelines(new_content)

    print(f"Content written to {file_path}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py "
              "[-d directory_parts] [-f filename]")
        sys.exit(1)

    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        for i in range(d_index + 1, len(args)):
            if args[i] == "-f":
                break
            directory_parts.append(args[i])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    if directory_parts:
        directory_path = create_directories(directory_parts)
        if file_name:
            file_path = os.path.join(directory_path, file_name)
            write_to_file(file_path)
        else:
            print(f"Directory created at: {directory_path}")
    elif file_name:
        write_to_file(file_name)
    else:
        print("Invalid arguments. Use -d "
              "for directories or -f for file creation.")


if __name__ == "__main__":
    main()
