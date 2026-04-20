import argparse
import os
import datetime


def create_directory(directory_name: str) -> None:
    os.makedirs(directory_name, exist_ok=True)


def create_file(file_name: str) -> None:

    with open(file_name, "a") as file:
        if os.stat(file_name).st_size > 0:
            file.write("\n")
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{create_time}\n")

        lines = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"Line{lines}: {new_line}\n")
            lines += 1


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")

    args = parser.parse_args()

    if args.directory:
        base_directory = os.path.join(*args.directory)
        create_directory(base_directory)

    if args.file:
        file_name = args.file
        if args.directory:
            os.chdir(base_directory)
        create_file(file_name)


if __name__ == "__main__":
    main()
