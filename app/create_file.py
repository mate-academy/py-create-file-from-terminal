import argparse
from datetime import datetime
import os


def management_by_terminal() -> None:
    parser = argparse.ArgumentParser("cmd from terminal")

    parser.add_argument("-d", nargs="+", help="Create directories")
    parser.add_argument("-f", help="Create or update file")

    args = parser.parse_args()

    if args.d is not None and args.f is not None:
        create_dir(args.d)
        current_path = os.path.join(*args.d, args.f)
        create_file(current_path)

    elif args.d is not None:
        create_dir(args.d)

    elif args.f is not None:
        create_file(args.f)


def create_dir(dirs: list) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    if file_path is not None:
        with open(file_path, "a") as file:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_date}\n")
            line = 1

            while True:
                user_input = input("Enter content line: ")
                if user_input.lower() == "stop":
                    break
                file.write(f"{line} Line{line} {user_input}" + "\n")
                line += 1
            file.write("\n")
        print(f"File created/updated: {file_path}")
    else:
        print("No file path provided. Use the -f option to specify a file.")


if __name__ == "__main__":
    management_by_terminal()
