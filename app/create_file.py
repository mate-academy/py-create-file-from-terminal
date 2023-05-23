import os
import sys
from datetime import datetime

command = sys.argv


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        line_number = 1
        while True:
            line_number += 1
            line_text = input("Enter content line: ")
            if line_text == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {line_text}\n")


def creating_file_from_command() -> None:
    if "-f" in command:
        if "-d" in command:
            command.pop(command.index("-f"))
            os.makedirs(os.path.join(*command[2:-1]), exist_ok=True)
            create_file(os.path.join(*command[2:]))
        else:
            create_file(command[command.index("-f") + 1])
    elif "-d" in command:
        os.makedirs(os.path.join(*command[2:]), exist_ok=True)


if __name__ == "__main__":
    creating_file_from_command()
