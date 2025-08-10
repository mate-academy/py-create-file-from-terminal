import os
from datetime import datetime
from sys import argv

command = argv


def creating_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        line_number = 1
        while True:
            line_number += 1
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line}\n")


def creating_file_from_command() -> None:
    if "-f" in command:
        if "-d" in command:
            command.pop(command.index("-f"))
            os.makedirs(os.path.join(*command[2:-1]), exist_ok=True)
            creating_file(os.path.join(*command[2:]))
        else:
            creating_file(command[command.index("-f") + 1])
    elif "-d" in command:
        os.makedirs(os.path.join(*command[2:]), exist_ok=True)


if __name__ == "__main__":
    creating_file_from_command()
