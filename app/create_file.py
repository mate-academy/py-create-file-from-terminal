import os
import sys
from datetime import datetime


def write_to_file_by_console(path: str) -> None:
    """Write lines to a file from console input until 'stop' is entered."""
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%y-%m-%d %H:%M:%S\n"))
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(line + "\n")


def write_to_file(path: str, text: str) -> None:
    """Append text to the specified file."""
    with open(path, "a") as file:
        file.write(text)


def main():
    args = sys.argv[1:]

    if "-f" not in args:
        print("Error: Missing required argument '-f' for filename.")
        sys.exit(1)

    filename = args[args.index("-f") + 1]

    if "-d" in args:
        # Handle directory path if specified
        try:
            d_index = args.index("-d") + 1
            dir_path = os.path.join(*args[d_index:args.index("-f")])
            os.makedirs(dir_path, exist_ok=True)
            path = os.path.join(dir_path, filename)
        except ValueError:
            print("Error: Invalid usage of '-d' argument.")
            sys.exit(1)
    else:
        # Default to the current directory if '-d' is not provided
        path = filename

    if not os.path.exists(path):
        print(f"Creating new file: {path}")
    else:
        print(f"Appending to existing file: {path}")

    write_to_file_by_console(path)


if __name__ == "__main__":
    main()
