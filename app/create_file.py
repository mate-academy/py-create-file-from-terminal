import argparse
import datetime
import os


def create_directory_structure(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_name: str, path: str = None) -> None:
    if path:
        full_path = os.path.join(path, file_name)
    else:
        full_path = os.path.join(os.getcwd(), file_name)

    file_exists = os.path.exists(full_path)
    file_is_empty = not file_exists or os.path.getsize(full_path) == 0

    with open(full_path, "a+") as file_path:
        if file_exists and not file_is_empty:
            file_path.write("\n")
        local = datetime.datetime.now()
        file_path.write(local.strftime("%m-%d-%Y %H:%M:%S\n"))
        line_numbering = 0
        lines = []
        while True:
            line = input("Enter content line (type 'stop' to finish): ")
            if line == "stop":
                break
            line_numbering += 1
            lines.append(f"{line_numbering} {line}")
        file_path.write("\n".join(lines))


def parse_arguments() -> None:
    parser = argparse.ArgumentParser(
        description="Create a directory and/or a file "
                    "within it with timestamp and user-provided content."
    )
    parser.add_argument(
        "-d", "--directory",
        nargs="+",
        help="Path to directory where the file will be created."
    )
    parser.add_argument("-f", "--file", help="Name of the file to be created.")
    args = parser.parse_args()

    if args.directory:
        directory_path = os.path.join(*args.directory)
        create_directory_structure(path=directory_path)

    if args.file:
        create_file(
            file_name=args.file,
            path=directory_path if args.directory else None
        )


if __name__ == "__main__":
    parse_arguments()
