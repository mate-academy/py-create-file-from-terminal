import sys
import os
from datetime import datetime


def create_directory(directory_path: str) -> None:
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, directory_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"Directory structure '{full_path}' created.")


def create_file(name: str) -> None:
    directory = os.path.dirname(name)
    if directory and not os.path.exists(directory):
        create_directory(directory)

    file_exists = os.path.exists(name)

    with open(name, "a" if file_exists else "w") as text_file:
        if not file_exists:
            current_time = datetime.now()
            formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            text_file.write(f"Created on: {formatted_timestamp}\n")

        line_number = 1
        while True:
            temp = input(f"Enter line {line_number} of content (or type 'stop' to finish): ")
            if temp.lower() == "stop":
                break
            text_file.write(f"{line_number}. {temp}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("No arguments provided. Please provide either '-d' or '-f' flags.")
        return

    if "-d" in args and "-f" in args:
        try:
            d_index = args.index("-d")
            f_index = args.index("-f")
            dir_path = os.path.join(*args[d_index + 1:f_index])
            file_name = args[f_index + 1]
            create_directory(dir_path)
            create_file(os.path.join(dir_path, file_name))
        except IndexError:
            print("Error: Missing arguments for directory or file.")
        return

    elif args[0] == "-d":
        args.pop(0)
        result_str = os.path.join(*args)
        create_directory(result_str)
        return

    elif args[0] == "-f":
        if len(args) > 1:
            create_file(args[1])
        else:
            print("Error: Missing file name after '-f' flag.")
        return


if __name__ == "__main__":
    main()
