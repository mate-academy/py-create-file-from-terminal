import os
import sys
from datetime import datetime


class InvalidInputCommand(Exception):
    pass


def create_dir(directory_way: list) -> str:
    path = os.path.join(*directory_way)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str) -> None:
    formated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_number = 1
    with open(file_name, "a") as f:
        if os.stat(file_name).st_size > 0:
            f.write("\n")
        f.write(f"{formated_time}\n")

        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1


def input_checker(commands: list) -> None:
    if "-f" and "-d" not in commands:
        raise InvalidInputCommand("Program takes min 1 arg '-f' or '-d', "
                                  "but 0 was given or arg not exist")
    if "-f" and "-d" in commands:
        flags = [commands.index("-f"), commands.index("-d")]
        if max(flags) - min(flags) == 1:
            raise InvalidInputCommand("Wrong flags position, "
                                      "should be '-d dir -f filename'")


def main() -> None:
    global directory
    commands = sys.argv

    try:
        input_checker(commands[1:])
    except Exception as err:
        print(err)
    else:
        if "-d" in commands:
            directory_way = (commands[2:]
                             if "-f" not in commands
                             else commands[2:-2])
            directory = create_dir(directory_way)

        if "-f" in commands:
            file_name = commands[-1]
            os.chdir(directory if directory else os.getcwd())
            create_file(file_name)


if __name__ == "__main__":
    main()
