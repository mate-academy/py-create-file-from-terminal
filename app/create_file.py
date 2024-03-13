import sys
import os
import datetime


class ArgumentError(Exception):
    pass


def create_dir(dir_parts: list[str]) -> str:
    directory = os.path.join(*dir_parts)
    os.makedirs(directory, exist_ok=True)
    return directory


def write_to_file(directory: str, file_name: str) -> None:
    with open(os.path.join(directory, file_name), "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = input("Enter content line: ")
        line_number = 1
        while line != "stop":
            file.write(f"{line_number}. {line}\n")
            line_number += 1
            line = input("Enter content line: ")
        if line_number > 1:
            file.write("\n")


if __name__ == "__main__":
    argv = sys.argv[1:]
    if "-f" not in argv and "-d" not in argv:
        raise ArgumentError("you need arguments like -f or -d.")

    index_of_f = argv.index("-f") if "-f" in argv else None
    index_of_d = argv.index("-d") if "-d" in argv else None

    if index_of_f is not None and index_of_f + 1 < len(argv):
        file_name = argv[index_of_f + 1]
    else:
        file_name = None
    if index_of_d is not None and index_of_d + 1 < len(argv):
        if index_of_f is not None and index_of_f > index_of_d + 1:
            dir_parts = argv[index_of_d + 1:index_of_f]
        else:
            dir_parts = argv[index_of_d + 1:]
    else:
        dir_parts = None

    if file_name and dir_parts:
        created_dir = create_dir(dir_parts)
        write_to_file(created_dir, file_name)
    elif file_name:
        write_to_file(os.getcwd(), file_name)
    elif dir_parts:
        create_dir(dir_parts)
