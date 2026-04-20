import os
import sys
from datetime import datetime, timezone, timedelta


def get_arguments():
    arguments = sys.argv
    directory_names = []
    file_name = ""

    if "-d" in arguments:
        d_index = arguments.index("-d")
        for arg in arguments[d_index + 1:]:
            if arg == "-f":
                break
            directory_names.append(arg)

    if "-f" in arguments:
        f_index = arguments.index("-f")
        if f_index + 1 < len(arguments):
            file_name = arguments[f_index + 1]

    return directory_names, file_name


def get_content():
    content_lines = []
    counter = 1
    while True:
        line = input(f"Line N:{counter} - Enter line: ")
        if line == "stop":
            break
        content_lines.append(line)
        counter += 1
    return content_lines


def save_to_file(directory_names, file_name, content_lines):
    full_path = ""
    if directory_names:
        full_path = os.path.join(*directory_names)
        os.makedirs(full_path, exist_ok=True)

    target_file = os.path.join(full_path, file_name)

    with open(target_file, "a") as output_file:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        output_file.write(f"{timestamp}\n")

        line_number = 1
        for line in content_lines:
            output_file.write(f"{line_number} {line}\n")
            line_number = line_number + 1

        output_file.write("\n")


def main():
    folder_parts, name = get_arguments()

    if not name:
        print("No arguments (-f 'filename', -d 'dir1' 'dir2' -> dir1/dir2/filename')")
        return

    lines = get_content()
    save_to_file(folder_parts, name, lines)


if __name__ == "__main__":
    main()