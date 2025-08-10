import os.path
import argparse
import datetime


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line = 1
        while True:
            line_content = input("Enter content line: ")
            if line_content.lower() == "stop":
                file.write(f"{line} {line_content}\n")
                break
            file.write(f"{line} {line_content}\n")
            line += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file", nargs="+")

    command_args = parser.parse_args()
    dir_path = None

    if command_args.directory:
        dir_path = str(os.path.join(*command_args.directory))
        os.makedirs(dir_path, exist_ok=True)
    else:
        print("Use -d to create directory")

    if command_args.file:
        file_path = str(os.path.join(*command_args.file))
        if dir_path:
            file_path = str(os.path.join(dir_path, file_path))
        create_file(file_path)
    else:
        print("Use '-f' to create file.")
