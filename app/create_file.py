import sys
import os
from datetime import datetime


def create_file(directory: str, filename: str, content: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_timestamp = f"{timestamp}\n{content}"
    file_path = os.path.join(directory, filename)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, "a") as file:
        file.write(content_with_timestamp + "\n")


def handle_d_flag(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")


def handle_f_flag(directory: str, filename: str) -> None:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
        content = "\n".join(content_lines)
        create_file(directory, filename, content)


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
