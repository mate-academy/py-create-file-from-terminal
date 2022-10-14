import argparse
import datetime
import os


def make_directory(*dir_path) -> None:
    os.makedirs(os.path.join(*dir_path), exist_ok=True)


def add_content_to_file(*path) -> None:
    current_time = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")

    with open(os.path.join(*path), "a") as file:
        file.write(f"{current_time}\n")
        num_line = 0
        content = input("Enter content line: ")
        while content.lower() != "stop":
            num_line += 1
            file.write(f"{num_line} {content}\n")
            content = input("Enter content line: ")

        file.write("\n")


def create_directory_and_file() -> None:
    parse = argparse.ArgumentParser()
    parse.add_argument("-d", nargs="*")
    parse.add_argument("-f", nargs=1)

    args = vars(parse.parse_args())

    if args["d"]:
        make_directory(*args["d"])

    if args["f"]:
        add_content_to_file(os.path.join(*args["d"] or [], *args["f"]))


create_directory_and_file()
