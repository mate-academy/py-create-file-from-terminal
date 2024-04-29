import os
import sys
from datetime import datetime


def create_directory(dirs: list) -> bool:
    path = os.path.join(*dirs)
    if os.path.exists(path):
        return False
    else:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created: {path}")
        return True


def create_file(file_name: str, dirs: list = None) -> None:
    if dirs:
        file_name = os.path.join(*dirs, file_name)
    user_input = get_user_input()
    with open(file_name, "a") as file:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_date}\n")
        line = 1

        for input_line in user_input:
            file.write(f"{line} Line{line} {input_line}" + "\n")
            line += 1

        file.write("\n")


def get_user_input() -> list:
    user_data = []
    while True:
        user_input = input("Write your content or enter 'stop' to exit: ")
        if user_input == "stop":
            break
        user_data.append(user_input)
    return user_data


def choice_of_creation(dirs: list | None, file_name: str | None) -> None:
    if dirs and file_name:  # dir and file
        if not create_directory(dirs):
            create_file(file_name, dirs)
    elif not file_name:  # dir
        if not create_directory(dirs):
            print("Directory already exists")
    elif not dirs:  # file
        create_file(file_name)


def check_presence_of_dirs_and_file(dirs_len: int = None,
                                    file_len: int = None) -> bool:
    if dirs_len is not None and dirs_len < 1:
        print("You forgot to enter directory name")
        return False
    elif file_len is not None and file_len <= 1:
        print("You forgot to enter file name")
        return False
    return True


def main() -> None:
    args = sys.argv[1:]
    dirs, file_name = None, None

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")

        if dir_index > file_index:
            print("Incorrect command order. "
                  "Please define file after directory")
            return

        if not check_presence_of_dirs_and_file(
                file_len=len(args[file_index:])
        ):
            return

        dirs = args[dir_index + 1:file_index]
        if not check_presence_of_dirs_and_file(dirs_len=len(dirs)):
            return

        file_name = args[file_index + 1]

    elif "-f" not in args:  # "-d" in args
        dir_index = args.index("-d")
        if not check_presence_of_dirs_and_file(dirs_len=len(args[dir_index:])):
            return
        dirs = args[dir_index + 1:]

    elif "-d" not in args:  # "-f" in args
        file_index = args.index("-f")
        if not check_presence_of_dirs_and_file(
                file_len=len(args[file_index:])
        ):
            return
        file_name = args[file_index + 1]

    choice_of_creation(dirs, file_name)


if __name__ == "__main__":
    main()
