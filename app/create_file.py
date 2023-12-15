import argparse
import os


def append_file_line(full_path_plus_filename: str) -> None:
    with open(full_path_plus_filename, "a") as file:
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            file.write(input_line + "\n")


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs='*', action="store", dest="file_directory")
    parser.add_argument("-f", "--filename", action="store", dest="file_name")
    args = parser.parse_args()

    full_path = ""
    if args.file_directory:
        full_path = os.path.join(*args.file_directory)
        os.makedirs(full_path, exist_ok=True)
    if args.file_name:
        full_path_plus_filename = os.path.join(full_path, args.file_name)
        append_file_line(full_path_plus_filename)


if __name__ == "__main__":
    create_file()
