import os
from datetime import datetime


def create_file(file_name: str) -> None:

    with open(file_name, "a+") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(line)
            file.write("\n")


def create_dir(dir1: str, dir2: str) -> None:
    direction = os.path.join(f"{dir1}/{dir2}")
    os.makedirs(direction, exist_ok=True)


def make_dir_and_file(dir1: str, dir2: str, file_name: str) -> None:
    direction = os.path.join(f"{dir1}/{dir2}")
    os.makedirs(direction, exist_ok=True)
    file_name = os.path.join(direction, file_name)
    create_file(file_name)


def user_management_cli() -> None:
    while True:
        terminal = input(">>>")
        command = terminal.split()
        if "-d" in command and "-f" in command:
            make_dir_and_file(command[3], command[4], command[6])
        elif "-d" in command:
            create_dir(command[3], command[4])
        elif "-f" in command:
            create_file(command[3])
        elif terminal == "stop":
            print("Exiting")
            break
        else:
            print("Unsupported command!")


if __name__ == "__main__":
    user_management_cli()
