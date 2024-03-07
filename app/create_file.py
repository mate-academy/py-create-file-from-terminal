import datetime
import os
import sys


def create_directory(directory: str) -> str:
    check_the_path = directory.split()
    if check_the_path[0] == "-d":
        check_the_path.remove(check_the_path[0])
        path = "/".join(check_the_path)
        os.makedirs(path, exist_ok=True)
        return path


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        is_true = True
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write("\n" + str(current_time) + "\n")
        line_number = 1
        while is_true:
            user_input = input("Enter content line: ")
            if user_input != "stop":
                file.write(f"{line_number}. {user_input} \n")
                line_number += 1
            else:
                is_true = False


def create_file_in_directory(directory: list, file_name: str) -> None:
    str_directory = " ".join(directory)
    directory_for_file = create_directory(str_directory)
    file_in_directory = directory_for_file + "/" + file_name
    create_file(file_in_directory)


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        reformat = str(args)
        create_directory(reformat)
    elif "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        create_file(file_name)
    if "-d" in args and "-f" in args:
        file_index = args.index("-f") + 1
        directory_paths = args[:file_index - 1]
        file_name = args[file_index]
        create_file_in_directory(directory_paths, file_name)


if __name__ == "__main__":
    main()
