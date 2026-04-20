import sys
import os
import datetime


def create_dir(args: list) -> str:
    path = os.path.join(*args)
    os.makedirs(path, exist_ok=True)

    return path


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        line_counter = 1

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                file.write("\n")
                break

            file.write(f"{line_counter} {line}\n")
            line_counter += 1


def read_arguments_from_terminal(args: list) -> None:
    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        if d_index < f_index:
            dir_path = create_dir(args[d_index + 1: f_index])
        else:
            dir_path = create_dir(args[d_index + 1: len(args)])

        file_path = os.path.join(dir_path, args[f_index + 1])
        create_file(file_path)

    elif "-d" in args:
        create_dir(args[args.index("-d") + 1: len(args)])

    elif "-f" in args:
        create_file(args[args.index("-f") + 1])


if __name__ == "__main__":
    read_arguments_from_terminal(sys.argv)
