import sys
import os
from datetime import datetime


def write_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as output_file:
        date = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        output_file.write(f"{date}\n")
        page_number = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            output_file.write(f"{page_number} {text}\n")
            page_number += 1
        output_file.write("\n")


def create_file(commands: list) -> None:
    """
    :param commands: list of commands
    :return: None

    This function is creating a directory or file.
    You have to use -d to create a directory or -f to create a file.
    You can use both arguments if you want to create file in some directory.
    Examples of usage parameter -d:

        "create_file.py -d dir1"
        "create_file.py -d dir1 dir2 ..."

    Example of usage parameter -f:
        "create_file.py -f file.txt"
    Also using -f you can write text to a file or write "stop" to stop writing.

    You can combine this parameters like in example:
        "create_file.py -d dir1 -f file.txt"
    """
    if "-help" in commands:
        print(create_file.__doc__)
        return

    path = ""
    if "-f" not in commands and "-d" not in commands:
        raise ValueError("You didn`t choose right command! "
                         "Use -help to see the usage of program.")

    if "-d" in commands:
        last_index_of_dirs = -1
        if "-f" in commands:
            last_index_of_dirs = commands.index("-f")

        path = os.path.join(*commands[1:last_index_of_dirs])
        os.makedirs(path, exist_ok=True)

    if "-f" in commands:
        path_to_file = os.path.join(path, commands[-1])
        write_file(path_to_file)


commands = sys.argv

if __name__ == "__main__":
    create_file(commands[1:])
