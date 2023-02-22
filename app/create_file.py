import os
import sys
from datetime import datetime


def create_path(commands_path: list) -> None:
    if commands_path:
        path = [folder for folder in commands_path]
        path = os.path.join(*path)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Path: '{path}' has been created")


def create_file(commands_file: list) -> None:
    if commands_file:
        output_file = commands_file[0].strip()
        with open(output_file, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
            line = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    file.write("\n")
                    print(f"{output_file} has been updated")
                    break
                file.write(f"{line} {content}\n")
                line += 1


commands = sys.argv[1:]
commands = " ".join(commands).split("-f")
commands_path = commands.pop(0).strip("-d").split()


if __name__ == "__main__":
    create_path(commands_path)
    create_file(commands)
