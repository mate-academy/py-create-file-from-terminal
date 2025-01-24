import sys
import os
from datetime import datetime


def create_directory(directory_path: str) -> None:

    current_dir = os.getcwd()

    full_path = os.path.join(current_dir, directory_path)

    os.makedirs(full_path, exist_ok=True)


def create_file(name: str) -> None:

    directory = os.path.dirname(name)
    if directory and not os.path.exists(directory):
        create_directory(directory)

    if os.path.exists(name):

        text_file = open(name, "a")
        current_time = datetime.now()
        formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        text_file.write(formatted_timestamp + "\n")
        while True:
            temp = input("Enter new line of content: ")
            if temp == "stop":
                text_file.close()
                break
            text_file.write(temp + "\n")
        return

    text_file = open(name, "w")
    current_time = datetime.now()
    formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    text_file.write(formatted_timestamp + "\n")
    while True:
        temp = input("Enter new line of content: ")
        if temp == "stop":
            text_file.close()
            break
        text_file.write(temp + "\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        dir_path = "/".join(args[d_index + 1:f_index])
        file_name = args[f_index + 1]

        create_directory(dir_path)
        create_file(os.path.join(dir_path, file_name))
        return

    elif args[0] == "-d":
        args.pop(0)
        result_str = "/".join(args)
        create_directory(result_str)
        return

    elif args[0] == "-f":
        create_file(args[1])
        return


if __name__ == "__main__":
    main()
