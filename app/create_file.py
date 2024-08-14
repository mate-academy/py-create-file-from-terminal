import argparse
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        print("(to stop the program write 'stop')")
        line_counter = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_counter} {line}\n")
            line_counter += 1

    print(f"File {file_path} created successfully.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", nargs="*", help="Directory path")
    parser.add_argument("-f", "--file", help="File path")
    args = parser.parse_args()

    directory_path = ""

    if args.dir:
        directory_path = os.path.join(*args.dir)
        os.makedirs(directory_path)
        print(f"{directory_path} directory created.")

    if args.file:
        file_path = os.path.join(directory_path, args.file)
        create_file(file_path)

    if not args.dir and not args.file:
        parser.error("Neither '-d' nor '-f' flag provided.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
