import sys
import os
from datetime import datetime


def create_file(name_file: str) -> None:
    if os.path.exists(name_file):
        command = "a"
    else:
        command = "w"
    with open(name_file, command) as f:
        f.write(str(datetime.strptime("2022-02-01 14:41:10",
                                      "%Y-%m-%d %H:%M:%S")) + "\n")
        count = 1
        while True:
            input_text = input("Enter content line: ")
            if input_text == "stop":
                break
            f.write(str(count) + " " + input_text + "\n")
            count += 1
        f.write("\n")


def create_direction(command_file: list) -> str:
    direction = command_file
    current_path = os.getcwd() + "/"
    for folder in direction:
        if not os.path.exists(current_path + folder):
            current_path = current_path + folder + "/"
            os.mkdir(current_path)
    return current_path


def create_file_in_direction(command_file: list) -> None:
    if "-f" in command_file[command_file.index("-d"):]:
        name_file = create_direction(command_file[command_file.index("-d") + 1:
                                                  command_file.index("-f")])
    else:
        name_file = create_direction(command_file[command_file.index("-d")
                                                  + 1:])
    create_file(name_file + command_file[command_file.index("-f") + 1])


def main() -> None:
    command_file = sys.argv
    if "-d" in command_file and "-f" in command_file:
        create_file_in_direction(command_file)
    elif command_file[1] == "-d":
        create_direction(command_file[2:])
    elif command_file[1] == "-f":
        create_file(command_file[2])


if __name__ == "__main__":
    main()
