from datetime import datetime
from sys import argv
from os import makedirs, path


def create_file() -> None:
    try:
        new_file_name = argv.pop(argv.index("-f") + 1)

        argv.pop(argv.index("-f"))
    except (IndexError, ValueError):
        create_dir()
    else:
        path_new_file = path.join(create_dir(), new_file_name)

        with open(path_new_file, "a") as new_file:
            new_file.write(making_content())


def create_dir() -> str:
    try:
        dir_file = path.join(
            *argv[argv.index("-d") + 1:]
        )
    except (IndexError, ValueError, TypeError):
        dir_file = ""
    else:
        makedirs(dir_file, exist_ok=True)

    return dir_file


def making_content() -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}\n"
    line_count = 0

    while True:
        user_input = input("Enter content line: ")

        if user_input == "stop":
            break

        line_count += 1
        content += f"{line_count} {user_input}\n"

    return f"{content}\n"


if __name__ == "__main__":
    create_file()
