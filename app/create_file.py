from datetime import datetime
import os
import argparse


def write_from_input(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [timestamp]
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    with open(file_path, "a", encoding="utf-8") as file:
        file.write("\n" + "\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create file and/or directories and write content into file.")
    parser.add_argument(
        "-d", "--dirs", nargs="+",
        help="Directory path(s) to create", default=[]
    )
    parser.add_argument(
        "-f",
        "--file", help="File name to create/write to"
    )

    args = parser.parse_args()

    # Create directory if -d is used
    full_dir_path = ""
    if args.dirs:
        full_dir_path = os.path.join(*args.dirs)
        try:
            os.makedirs(full_dir_path, exist_ok=True)
        except Exception as e:
            print(f"Error creating directories: {e}")
            return

    # If file is specified
    if args.file:
        file_path = os.path.join(full_dir_path, args.file) \
            if full_dir_path \
            else args.file
        try:
            write_from_input(file_path)
        except Exception as e:
            print(f"Error writing to file: {e}")
    elif not args.dirs:
        print("Error: You must provide at least -f (filename) or -d (directory path).")


if __name__ == "__main__":
    main()
