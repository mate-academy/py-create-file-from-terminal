import sys
from os import mkdir
from time import localtime, strftime


def create_file_from_command_line(args):
    create_dir = False
    create_file = False
    directory = ""
    for arg in args:
        if arg == "-f":
            create_file = True
            create_dir = False
            continue
        if arg == "-d":
            create_dir = True
            create_file = False
            continue
        if create_file:
            with open(f"{directory}{arg}", "w") as file_created:
                print(strftime("%Y-%m-%d %H:%M:%S", localtime()), file=file_created)
                line = 1
                while True:
                    text = input("Enter content line: ")
                    if text == "stop":
                        break
                    print(f"{line} {text}", file=file_created)
                    line += 1
            create_file = False
        if create_dir:
            directory += f"{arg}/"
            mkdir(directory)


if __name__ == "__main__":
    create_file_from_command_line(sys.argv)
