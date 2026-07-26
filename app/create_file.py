import argparse
import os
import datetime


def create_directories(directories_to_create: str, create_path: str) -> str:
    if directories_to_create is not None:
        for folder in directories_to_create:
            try:
                os.mkdir(os.path.join(create_path, folder))
            except FileExistsError:
                pass
            create_path = os.path.join(create_path, folder)
    return create_path


def write_in_file(file_name: str, path_of_file: str) -> None:
    if file_name is not None:
        with open(os.path.join(path_of_file, file_name), "a") as f:
            f.write(
                datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
            line_count = 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    f.write("\n")
                    break
                f.write(f"{line_count} {line} \n")
                line_count += 1


def parse_command() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file_name")
    parser.add_argument("-d", "--directories_to_create", nargs="+")

    args = parser.parse_args()
    current_path = os.getcwd()

    current_path = create_directories(args.directories_to_create, current_path)
    write_in_file(args.file_name, current_path)


if __name__ == "__main__":
    parse_command()
