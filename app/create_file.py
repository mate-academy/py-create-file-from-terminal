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


if __name__ == "__main__":
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")

        if d_index < f_index:
            dir_path = create_dir(sys.argv[d_index + 1: f_index])
        else:
            dir_path = create_dir(sys.argv[d_index + 1: len(sys.argv)])

        file_path = os.path.join(dir_path, sys.argv[f_index + 1])
        create_file(file_path)

    elif "-d" in sys.argv:
        create_dir(sys.argv[sys.argv.index("-d") + 1: len(sys.argv)])

    elif "-f" in sys.argv:
        create_file(sys.argv[sys.argv.index("-f") + 1])
