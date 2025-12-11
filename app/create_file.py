import sys
import os
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_content():
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_content(file_path, lines):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(get_timestamp() + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")
        f.write("\n")  # Blank line after each block


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2 ...")
        print("  python create_file.py -f filename")
        print("  python create_file.py -d dir1 dir2 -f filename")
        return

    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # Read all directory parts until hitting -f or end
            while i < len(args) and args[i] != "-f":
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                print("Error: -f flag must be followed by a file name.")
                return
        else:
            i += 1

    # Construct directory path if -d was used
    dir_path = ""
    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    # Handle file creation
    if file_name:
        file_path = os.path.join(dir_path, file_name)\
            if dir_path else file_name

        # Ask user for content
        lines = read_content()

        # Write or append to file
        write_content(file_path, lines)

        print(f"File created/updated: {file_path}")

    else:
        # -d only case (no file)
        if dir_parts:
            print(f"Directory created: "
                  f"{dir_path}")
        else:
            print("Error: No valid "
                  "flags provided.")


if __name__ == "__main__":
    main()
