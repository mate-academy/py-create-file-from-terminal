import os
import sys
from datetime import datetime


def get_user_input() -> list:
    user_data = []
    while True:
        user_input = input("Write your content or enter 'stop' to exit: ")
        if user_input == "stop":
            break
        user_data.append(user_input)
    return user_data


def create_directory(dirs: list) -> None:
    try:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
    except TypeError:
        print("Please enter correct path")


def create_file(file_name: str, dirs: list = None) -> None:
    if dirs:
        file_name = os.path.join(*dirs, file_name)
    user_input = get_user_input()
    try:
        with open(file_name, "a") as file:
            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_date}\n")
            line = 1

            for input_line in user_input:
                file.write(f"{line} {input_line}" + "\n")
                line += 1

            file.write("\n")
    except Exception as exception:
        print("Can not create file: ", exception)


def choice_of_creation(dirs: list | None, file_name: str | None) -> None:
    if dirs and file_name:  # dir and file
        create_directory(dirs)
        create_file(file_name, dirs)
    elif not file_name:  # dir
        create_directory(dirs)
    elif not dirs:  # file
        create_file(file_name)


def main() -> None:
    args = sys.argv[1:]
    dirs, file_name = None, None

    try:
        if "-d" in args and "-f" in args:
            dir_index = args.index("-d")
            file_index = args.index("-f")
            dirs = args[dir_index + 1:file_index]
            file_name = args[file_index + 1]

        elif "-f" not in args:  # "-d" in args
            dir_index = args.index("-d")
            dirs = args[dir_index + 1:]

        elif "-d" not in args:  # "-f" in args
            file_index = args.index("-f")
            file_name = args[file_index + 1]
    except IndexError:
        print("You forgot to enter name of file")
        return

    choice_of_creation(dirs, file_name)


if __name__ == "__main__":
    main()
