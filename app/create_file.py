import os
import sys
import datetime


arguments = sys.argv


def create_file_command(args: list) -> None:
    dirs = ""

    if "-d" in args:
        if "-f" not in args or (
                "-f" in args and args.index("-d") > args.index("-f")):
            dirs = os.path.join(*args[args.index("-d") + 1:]) + "/"
        else:
            dirs = os.path.join(
                *args[args.index("-d") + 1:args.index("-f")]
            ) + "/"

        if not os.path.exists(dirs):
            os.makedirs(dirs)

    if "-f" in args:
        with open(dirs + args[args.index("-f") + 1], "a") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d"
                                                        " %H:%M:%S\n"))
        number_of_string = 1

        while True:
            string = input("Enter content line: ")

            if string == "stop":
                with open(dirs + args[args.index("-f") + 1], "a") as file:
                    file.write("\n")
                break

            with open(dirs + args[args.index("-f") + 1], "a") as file:
                file.write(f"{str(number_of_string)} {string}\n")

            number_of_string += 1


if __name__ == "__main__":
    create_file_command(arguments)
