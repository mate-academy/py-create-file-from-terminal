from sys import argv
import os
import datetime


def create_file() -> None:
    args_terminal = argv
    name_path_dirs = file_name = ""

    if "-d" in args_terminal:
        pos_dir = (args_terminal.index("-d")) + 1
        for i in range(pos_dir, len(args_terminal)):
            if args_terminal[i] == "-f":
                break
            name_path_dirs += args_terminal[i] + "/"

        os.makedirs(name_path_dirs, exist_ok=True)

    if "-f" in args_terminal:
        pos_name_file = args_terminal.index("-f")
        try:
            file_name = args_terminal[pos_name_file + 1]
        except IndexError("without name file after -f."):
            return IndexError

    path_file_complete_name = os.path.join(name_path_dirs, file_name)
    file_exist = os.path.exists(path_file_complete_name)

    with open(path_file_complete_name, "a") as file:
        if not file_exist:
            first_line = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(first_line + "\n")
        count = 1
        while 1:
            value_input = input("Enter content line: ")
            if value_input == "stop":
                break

            file.write(f"{count} {value_input}\n")
            count += 1


if __name__ == "__main__":
    create_file()
