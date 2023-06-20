import os
import sys
import datetime


def create_file() -> None:
    try:
        new_file = sys.argv.pop(sys.argv.index("-f") + 1)
        sys.argv.pop(sys.argv.index("-f"))
    except (IndexError, ValueError):
        create_directory()
    else:
        new_path = os.path.join(create_directory(), new_file)

        with open(new_path, "a") as new_file_path:
            new_file_path.write(make_content())


def create_directory() -> str:
    try:
        dir_file = os.path.join(sys.argv[sys.argv.index("-d") + 1:])
    except (TypeError, ValueError):
        dir_file = ""
    else:
        os.makedirs(dir_file)

    return dir_file


def make_content() -> str:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}"
    while True:
        user_input = input("Enter content line: ")
        while user_input != "stop":
            content += f"{user_input}"
        return content


if __name__ == "__main__":
    create_file()
