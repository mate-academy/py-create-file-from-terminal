import datetime
import os
import argparse


def work_with_file(file_path: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}\n"

    print("Enter content for new_file (Enter 'stop' to finish):")
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content += f"{line_number} {line}\n"
        line_number += 1

    with open(file_path, "a") as file:
        file.write(content + "\n")


def create_dirs(directories: list) -> str:
    directory = os.path.join(*directories)
    os.makedirs(directory, exist_ok=True)
    return directory


def parse_commands() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directories",
                        nargs="+",
                        help="Enter directories for the file")
    parser.add_argument("-f", "--filename", help="Enter the name of the file")
    args = parser.parse_args()

    filename = args.filename
    directories = args.directories if args.directories else []
    directory = create_dirs(directories) if directories else os.getcwd()

    if filename:
        file_path = os.path.join(directory, filename)
        work_with_file(file_path)
    else:
        print("Please provide the --filename argument to create a file.")


if __name__ == "__main__":
    parse_commands()
