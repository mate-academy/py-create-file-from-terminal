import os
import sys
import datetime


class CustomError(Exception):
    pass


user_input = sys.argv[1:]


def write_file(filename: str) -> None:
    header = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = []
    while True:
        user_choice = input("Enter content line: ")
        if user_choice == "stop":
            break
        lines.append(user_choice)
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "a") as file:
            file.write("\n")

    with open(filename, "a") as f:
        f.write(header + "\n")
        for number, line in enumerate(lines, 1):
            f.write(f"{number} {line}\n")


if len(user_input) == 0:
    raise ValueError("You must enter a command line argument: -f or -d")


elif "-d" in user_input and "-f" in user_input:
    d_index = user_input.index("-d")
    f_index = user_input.index("-f")
    if d_index > f_index:
        raise CustomError("You should enter a -d before -f")

    dir_path = user_input[d_index + 1 :f_index]
    if not dir_path:
        raise ValueError("No directories specified after -d")

    string_path = os.path.join(*dir_path)
    os.makedirs(string_path, exist_ok=True)

    file_name = user_input[f_index + 1]
    file_path = os.path.join(string_path, file_name)
    write_file(file_path)


elif user_input[0] == "-d":
    path = user_input[1:]
    string_path = os.path.join(*path)
    os.makedirs(string_path, exist_ok=True)


elif user_input[0] == "-f":
    file_name = user_input[-1]
    write_file(file_name)
