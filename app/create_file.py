import os
import sys
import datetime


arguments = sys.argv


def create_file_command(args: list) -> None:
    dirs = ""
    index_command_d = args.index("-d") if "-d" in args else None
    index_command_f = args.index("-f") if "-f" in args else None

    if "-d" in args:
        if "-f" not in args or (
                "-f" in args and index_command_d > index_command_f):
            dirs = os.path.join(*args[index_command_d + 1:]) + "/"
        else:
            dirs = os.path.join(
                *args[index_command_d + 1:index_command_f]
            ) + "/"

        os.makedirs(dirs, exist_ok=True)

    if "-f" in args:
        write_string = datetime.datetime.now().strftime("%Y-%m-%d"
                                                        " %H:%M:%S\n")
        number_of_string = 1

        while True:
            string = input("Enter content line: ")

            if string == "stop":
                write_string += "\n"
                break

            write_string += f"{str(number_of_string)} {string}\n"
            number_of_string += 1

        with open(dirs + args[index_command_f + 1], "a") as file:
            file.write(write_string)


if __name__ == "__main__":
    create_file_command(arguments)
