import sys
import os
from datetime import datetime

stop_word = "stop"
timestamp_format = "%Y-%m-%d %H:%M:%S"
dir_flag = "-d"
file_flag = "-f"


def get_timestamp() -> str:
    return datetime.now().strftime(timestamp_format)


def get_user_content() -> list:
    content_lines = []
    print("Enter content lines (type 'stop' to finish input):")

    while True:
        try:
            line = input("Enter content line: ")
        except EOFError:
            break

        if line.strip().lower() == stop_word:
            break

        content_lines.append(line)
    return content_lines


def format_new_block(content_lines: list) -> str:
    timestamp = get_timestamp()
    formatted_text = f"\n{timestamp}\n"
    for index, line in enumerate(content_lines, 1):
        formatted_text += f"{index} {line}\n"

    return formatted_text


def parse_args(args: list) -> tuple:
    dir_parts = []
    file_name = None

    i = 1
    while i < len(args):
        arg = args[i]

        if arg == dir_flag:
            i += 1
            while i < len(args) and args[i] not in [file_flag, dir_flag]:
                dir_parts.append(args[i])
                i += 1
            continue

        if arg == file_flag:
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            continue

        i += 1

    return dir_parts, file_name


def main():
    dir_parts, file_name = parse_args(sys.argv)

    if file_name is None:
        print(f"Error: File name is missing "
              f"or misplaced after the {file_flag} flag.")
        sys.exit(1)
    target_dir = os.path.join(*dir_parts) if dir_parts else ""
    if target_dir:
        try:
            os.makedirs(target_dir, exist_ok=True)
            print(f"Created/ensured directory: {target_dir}")
        except OSError as e:
            print(f"Error creating directory {target_dir}: {e}")
            sys.exit(1)
    if target_dir:
        full_file_path = os.path.join(target_dir, file_name)
    else:
        full_file_path = file_name
    new_content_lines = get_user_content()

    if not new_content_lines:
        print("No content entered. File operation aborted.")
        return
    formatted_content = format_new_block(new_content_lines)

    try:
        with open(full_file_path, "a", encoding="utf-8") as target_file:
            target_file.write(formatted_content)
        print(f"Content successfully appended to file: {full_file_path}")

    except IOError as e:
        print(f"Error writing to file {full_file_path}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
