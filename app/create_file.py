import os
import sys
import datetime


arguments = sys.argv


def create_file_command(args: list) -> None:
    dirs = ""

    if "-d" in args:
        if "-f" not in args:
            dirs = "/".join(args[args.index("-d") + 1:]) + "/"
        else:
            if args.index("-d") > args.index("-f"):
                dirs = "/".join(args[args.index("-d") + 1:]) + "/"
            else:
                dirs = "/".join(
                    args[args.index("-d") + 1:args.index("-f")]
                ) + "/"

        if not os.path.exists(dirs):
            os.makedirs(dirs)

    if "-f" in args:
        with open(dirs + args[args.index("-f") + 1], "a") as file:
            file.write(datetime.datetime.now().strftime("%Y-%m-%d "
                                                        "%H:%M:%S\n"))
            number_of_string = 1

            while True:
                string = input("Enter content line: ")

                if string == "stop":
                    file.write("\n")
                    break

                file.write(str(number_of_string) + " " + string + "\n")
                number_of_string += 1


create_file_command(arguments)
