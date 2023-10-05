import sys
import os
from datetime import datetime


def create_file(directory: str, filename: str,  content: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = os.path.join(directory, filename)
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(f"{timestamp}\n{len(content.splitlines())} Enter content line: {len(content.splitlines())} {content}")


def handle_d_flag(directory: str) -> None:
    nested_directory = os.path.join(directory, "dir2")
    if not os.path.exists(nested_directory):
        os.makedirs(nested_directory)
        print(f"Directory {nested_directory} created.")
    else:
        print(f"Directory {nested_directory} already exists.")


def handle_f_flag(directory: str, filename: str) -> None:
    nested_directory = os.path.join(directory, "dir1", "dir2")
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
        content = "\n".join(content_lines)
        create_file(nested_directory, filename, content)


def main() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = sys.argv[dir_index]
        handle_d_flag(directory)
    elif "-f" in sys.argv and "-d" not in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]
        handle_f_flag(".", filename)
    elif "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory = sys.argv[dir_index]
        filename = sys.argv[file_index]
        handle_d_flag(directory)
        handle_f_flag(directory, filename)
    else:
        print("Use -d or -f")
        return


if __name__ == "__main__":
    main()
