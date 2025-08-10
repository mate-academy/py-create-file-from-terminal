import argparse
import datetime
import os


def get_cli_arguments() -> argparse.PARSER:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dirs", nargs="*")
    parser.add_argument("-f", dest="file", nargs=1)
    return parser.parse_args()


def create_directories(dirs: list) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)


def create_file(file_name: list, dirs: list = None) -> None:
    path = (
        os.path.join(*dirs, *file_name) if dirs else os.path.join(*file_name)
    )
    with open(path, "a") as source_file:
        file_content = get_file_content()
        source_file.writelines(file_content)
        source_file.write("\n")


def get_file_content() -> list[str]:
    file_content = []
    current_time = get_current_time()
    file_content.append(f"{current_time}\n")

    row_counter = 0
    while True:
        row = input("Enter content line: ")
        row_counter += 1
        if row == "stop":
            break
        file_content.append(f"{row_counter} {row}\n")
    return file_content


def get_current_time() -> str:
    current_time = datetime.datetime.now()
    formatted_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_current_time


def main() -> None:
    cli_arguments = get_cli_arguments()

    if dirs := cli_arguments.dirs:
        create_directories(dirs)

    if file := cli_arguments.file:
        create_file(file, dirs)


if __name__ == "__main__":
    main()
