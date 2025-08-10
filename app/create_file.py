import os
import sys
import datetime


def get_time_stamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_user_input() -> list:
    content_lines = []
    while True:
        line = input("Enter content line (or 'stop' to finish): ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def create_file(file_path: str, content_lines: list) -> None:
    timestamp = get_time_stamp()
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(timestamp + "\n")
        for line_number, line in enumerate(content_lines, 1):
            file.write(f"{line_number} {line}\n")


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage: python create_file.py -d <directory_path>"
            " OR -f <file_name>"
        )
        sys.exit(1)

    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")

        if dir_index > file_index:
            print("Invalid usage: -f flag must come after -d flag.")
            sys.exit(1)

        directory_path = os.path.join(*sys.argv[dir_index + 1:file_index])
        file_name = sys.argv[file_index + 1]
        file_path = os.path.join(directory_path, file_name)
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        file_name = None
        file_path = None
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        directory_path = None
        file_name = sys.argv[file_index + 1]
        file_path = file_name
    else:
        print("You must specify either -d or -f flag.")
        sys.exit(1)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        new_content_lines = get_user_input()
        create_file(file_path, new_content_lines)
        print(f"File {file_path} created successfully.")


if __name__ == "__main__":
    main()
