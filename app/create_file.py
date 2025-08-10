import sys
import os
from datetime import datetime


def create_file_with_content(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            inputed_line = input("Enter content line: ")
            if inputed_line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {inputed_line}\n")
            line_number += 1


def create_directory(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        print(e)
        sys.exit(1)


def main() -> None:
    argv = sys.argv[1:]
    if "-f" in argv:
        try:
            file_index = argv.index("-f") + 1
            file_name = argv[file_index]
        except IndexError:
            print("Invalid data has been inputted")
            sys.exit(1)
        if "-d" in argv:
            try:
                dir_list = (argv[argv.index("-d") + 1: argv.index("-f")]
                            or argv[argv.index("-d") + 1: len(argv)])
                path = os.path.join(*dir_list)
                create_directory(path)
            except Exception as e:
                print(e)
                sys.exit(1)
            file_name = os.path.join(path, file_name)
            create_file_with_content(file_name)
    elif "-d" in argv:
        try:
            path = os.path.join(
                *[argv[arg_index]
                  for arg_index in range(1, len(argv))])
            create_directory(path)
        except TypeError:
            print("Missing directory name")


if __name__ == "__main__":
    main()
