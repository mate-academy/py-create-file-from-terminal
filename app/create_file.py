import sys
import os
from datetime import datetime


def parse_arguments():
    args = sys.argv[1:]

    if not args:
        print("Error: No arguments provided. Use -d for directory and/or -f for file.")
        sys.exit(1)

    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == '-d':
            i += 1
            while i < len(args) and args[i] != '-f':
                dir_parts.append(args[i])
                i += 1
        elif args[i] == '-f':
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                print("Error: -f flag requires a file name.")
                sys.exit(1)
        else:
            i += 1

    return dir_parts, file_name


def get_file_content():
    print()
    lines = []
    line_number = 1

    while True:
        content = input("Enter content line: ")
        if content.lower() == "stop":
            break
        lines.append(f"{line_number} {content}")
        line_number += 1

    return lines


def create_file_with_content(file_path, content_lines):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(file_path)

    with open(file_path, 'a') as f:
        if file_exists:
            f.write("\n")

        f.write(f"{timestamp}\n")

        for line in content_lines:
            f.write(f"{line}\n")

        f.write("\n")

    print(f"\nFile created/updated successfully: {file_path}")


def main():
    dir_parts, file_name = parse_arguments()

    if dir_parts:
        target_dir = os.path.join(*dir_parts)
        os.makedirs(target_dir, exist_ok=True)
        print(f"Directory created/verified: {target_dir}")
    else:
        target_dir = "."

    if file_name:
        content_lines = get_file_content()

        if content_lines:
            file_path = os.path.join(target_dir, file_name)
            create_file_with_content(file_path, content_lines)
        else:
            print("\nNo content entered. File not created.")
    elif dir_parts:
        print("Directory created successfully.")
    else:
        print("Error: Please specify -d for directory and/or -f for file.")


if __name__ == "__main__":
    main()