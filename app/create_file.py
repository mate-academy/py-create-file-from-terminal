import os
import sys
from datetime import datetime


def main() -> None:
    directory_parts = []
    file_name = None

    arg_index = 0
    while arg_index < len(sys.argv):
        if sys.argv[arg_index] == "-d":
            arg_index += 1
            while (arg_index < len(sys.argv)
                   and not sys.argv[arg_index].startswith("-")):
                directory_parts.append(sys.argv[arg_index])
                arg_index += 1
            continue

        if sys.argv[arg_index] == "-f":
            if arg_index + 1 < len(sys.argv):
                file_name = sys.argv[arg_index + 1]
                arg_index += 2
                continue

        arg_index += 1

    target_directory = os.path.join(*directory_parts)\
        if directory_parts else "."

    if directory_parts:
        os.makedirs(target_directory, exist_ok=True)

    if file_name:
        content_lines = []
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            content_lines.append(user_input)

        full_path = os.path.join(target_directory, file_name)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(full_path, "a", encoding="utf-8") as output_file:
            output_file.write(f"{timestamp}\n")
            for line_number, text in enumerate(content_lines, start=1):
                output_file.write(f"{line_number} {text}\n")


if __name__ == "__main__":
    main()
