import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage examples:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directory_parts = args[d_index + 1:f_index]
        else:
            directory_parts = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if len(args) > f_index + 1:
            file_name = args[f_index + 1]
        else:
            print("Error: No filename provided after -f")
            sys.exit(1)

    target_path = os.getcwd()
    if directory_parts:
        target_path = os.path.join(target_path, *directory_parts)
        os.makedirs(target_path, exist_ok=True)
        print(f"Directory created or already exists: {target_path}")

    if not file_name:
        print("No file specified. Only directory created.")
        sys.exit(0)

    file_path = os.path.join(target_path, file_name)

    print("\nEnter content line (type 'stop' to finish):")
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.strip().lower() == "stop":
            break
        lines.append(user_input)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n")
        output_file.write(f"{timestamp}\n")
        for line_number, content_line in enumerate(lines, start=1):
            output_file.write(f"{line_number} {content_line}\n")

    print(f"\nFile created/updated successfully at: {file_path}")


if __name__ == "__main__":
    main()
