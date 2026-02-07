import datetime
import os
import sys


def create_file() -> None:

    args = sys.argv
    args_index = 1
    dir_path = "."

    if args_index < len(args) - 1 and args[args_index] == "-d":

        args_index += 1

        while args_index < len(args) - 1 and args[args_index] != "-f":
            dir_path = os.path.join(dir_path, args[args_index])
            args_index += 1

        print(dir_path)
        os.makedirs(dir_path)

    if args_index < len(args) - 1 and args[args_index] == "-f":

        file_name = args[args_index + 1]
        line_num = 1
        with open(os.path.join(dir_path, file_name), "a") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

            while True:
                line = input("Enter content line: ")

                if line == "stop":
                    file.write("\n")
                    break

                file.write(f"{line_num} {line}\n")
                line_num += 1
    else:
        print("No file argument found")
