import argparse
import datetime
import os


def get_parser() -> None:
    parser = argparse.ArgumentParser(description="Create file from terminal")
    parser.add_argument(
        "-d",
        dest="directory_path",
        type=str,
        nargs="+",
        help="create directory"
    )
    parser.add_argument("-f", dest="file", type=str, help="create file")
    args = parser.parse_args()

    if args.directory_path and not args.file:
        create_directory(args.directory_path)
    if args.file and not args.directory_path:
        create_file(args.file_name)
    if args.file and args.directory_path:
        create_file_in_directory(args.directory_path, args.file)


def get_datetime() -> str:
    today = datetime.datetime.today()
    today = datetime.datetime.strftime(today, "%B %d, %Y. %H:%M:%S")
    return today


def create_file_in_directory(dir_path: list, file_name: str) -> None:
    dir_path = create_directory(dir_path)
    os.chdir(dir_path)
    create_file(file_name)


def create_directory(dir_path: list) -> str:
    dir_path = os.path.join(*dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def create_file(file_name: str) -> None:
    today = get_datetime()
    with open(file_name, "a") as content_file:
        content_file.write(today + "\n")
        number_of_string = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                content_file.write("\n")
                break
            content_to_write = f"{str(number_of_string)} {content}"
            content_file.write(content_to_write + "\n")
            number_of_string += 1


if __name__ == "__main__":
    get_parser()
