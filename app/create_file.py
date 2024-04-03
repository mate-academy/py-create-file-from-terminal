import os
import sys
import datetime


command: list = sys.argv


def create_dir() -> str:
    full_path: str = "."
    end_of_dir: int = command.index("-f") if "-f" in command \
        else len(command) + 1
    for part_path in command[command.index("-d") + 1:end_of_dir]:
        full_path = os.path.join(full_path, part_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def create_file(file_path: str = "") -> None:
    with open(
            os.path.join(file_path, command[command.index("-f") + 1]),
            "a"
    ) as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        while True:
            input_str: str = input("Enter content line: ")
            if input_str.lower() == "stop":
                file.write("\n")
                break
            file.write(input_str + "\n")


if __name__ == "__main__":
    if "-d" in command and "-f" in command:
        create_file(create_dir())
    elif "-d" in command:
        create_dir()
    elif "-f" in command:
        create_file()
    else:
        raise Exception("The command is not correct.")
