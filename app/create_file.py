import sys
import os
from datetime import datetime


def get_timestamp():
    """Return formatted current timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_directory(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def write_content_to_file(file_path):
    """Write user input content to the file, appending if it already exists."""
    print(f"Writing to file: {file_path}")

    content_lines = []
    line_number = 1

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(f"{line_number} {line}")
        line_number += 1

    if not content_lines:
        print("No content added. Exiting.")
        return

    timestamp = get_timestamp()

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")  # Separate sections if file already exists
        file.write(f"{timestamp}\n")
        file.write("\n".join(content_lines))
        file.write("\n")

    print(f"File updated: {file_path}")


def main():
    """Parse arguments and execute the required actions."""
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d") + 1
        f_index = sys.argv.index("-f") if "-f" in sys.argv else len(sys.argv)
        directory_path = os.path.join(*sys.argv[d_index:f_index])

        if directory_path:
            create_directory(directory_path)

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f") + 1
        if f_index < len(sys.argv):
            file_name = sys.argv[f_index]
        else:
            print("Error: No file name specified after -f")
            return

        file_path = file_name if "-d" not in sys.argv else os.path.join(directory_path, file_name)
        write_content_to_file(file_path)


if __name__ == "__main__":
    main()