import datetime
import os
import sys


def create_file() -> None:
    args = sys.argv[1:]
    dir_path = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    if dir_path:
        os.makedirs(os.path.join(*dir_path), exist_ok=True)

    if file_name:
        target_file_path = file_name
        if dir_path:
            target_file_path = os.path.join(*dir_path, target_file_path)
        write_lines(target_file_path)


def write_lines(file_path_to_write: str) -> None:
    line_counter = 0
    formatted_lines = []

    with open(file_path_to_write, "a") as destination_file:
        if destination_file.tell() > 0:
            destination_file.write("\n")

        destination_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )

        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            line_counter += 1
            formatted_lines.append(f"{line_counter} {user_input}\n")

        destination_file.writelines(formatted_lines)


create_file()
