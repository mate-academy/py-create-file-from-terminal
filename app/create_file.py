import os
import sys
from datetime import datetime


def create_directory(path_parts: list[str]) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created.")


def create_file(file_path: str) -> None:
    content_lines = []
    print("Enter content lines (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n\n")
        f.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")

    print(f"File '{file_path}' created/updated.")


def main() -> None:
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        path_parts = sys.argv[d_index + 1:]
        if not path_parts or "-f" in path_parts:
            print("Error: "
                  "Please provide a valid directory path after -d flag.")
            return
        create_directory(path_parts)

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        if "-d" in sys.argv:
            d_index = sys.argv.index("-d")
            path_parts = sys.argv[d_index + 1:f_index]
            create_directory(path_parts)
            file_name = sys.argv[f_index + 1]
            file_path = os.path.join(*path_parts, file_name)
        else:
            file_name = sys.argv[f_index + 1]
            file_path = file_name

        create_file(file_path)
    elif "-d" not in sys.argv:
        print("Error: Please provide a valid -d or -f flag.")


if __name__ == "__main__":
    main()
