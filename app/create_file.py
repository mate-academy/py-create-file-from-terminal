import sys
import os
from datetime import datetime

file_flag = "-f"
dir_flag = "-d"


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def parse_args(args: list) -> tuple[list, str | None]:
    dir_parts = []
    file_name = None

    args = args[1:]

    i = 0
    while i < len(args):
        if args[i] == dir_flag:
            i += 1
            while i < len(args) and args[i] not in (file_flag, dir_flag):
                dir_parts.append(args[i])
                i += 1
            continue

        elif args[i] == file_flag:
            i += 1
            if i < len(args) and args[i] not in (file_flag, dir_flag):
                file_name = args[i]
                i += 1
            continue

        i += 1

    return dir_parts, file_name


def get_user_content() -> list[str]:
    content_lines = []
    print("Enter content lines (type 'stop' to finish input):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def format_new_block(lines: list[str]) -> str:
    timestamp = get_timestamp()
    formatted_block = f"{timestamp}\n"
    for i, line in enumerate(lines, 1):
        formatted_block += f"{i} {line}\n"
    return formatted_block


def main() -> None:
    dir_parts, file_name = parse_args(sys.argv)

    target_dir = os.path.join(*dir_parts) if dir_parts else ""

    if target_dir:
        try:
            os.makedirs(target_dir, exist_ok=True)
            print(f"Created/ensured directory: {target_dir}")
        except OSError as e:
            print(f"Error creating directory ({target_dir}): {e}")
            sys.exit(1)

    if file_name is None:
        if not dir_parts:
            print(f"Error: File name is missing "
                  f"or misplaced after the {file_flag} flag.")
            sys.exit(1)
        else:
            return

    full_file_path = os.path.join(target_dir, file_name) \
        if target_dir else file_name

    new_content_lines = get_user_content()

    if not new_content_lines:
        print("No content entered. File operation aborted.")
        return

    formatted_content = format_new_block(new_content_lines)
    needs_separator = False
    if os.path.exists(full_file_path) and os.path.getsize(full_file_path) > 0:
        needs_separator = True

    final_write_content = ("\n" if needs_separator else "") + formatted_content

    try:
        with open(full_file_path, "a", encoding="utf-8") as f:
            f.write(final_write_content)
        print(f"Content successfully appended to file: {full_file_path}")
    except IOError as e:
        print(f"Error writing to file ({full_file_path}): {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
