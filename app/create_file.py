import sys
import os
import datetime

commands = sys.argv[1:]
commands = " ".join(commands).split("-f")
path = commands.pop(0).strip("-d").split()


def create_path(direction: list) -> None:
    if direction:
        direction = os.path.join(*direction)
        if not os.path.exists(direction) and len(direction) > 0:
            os.makedirs(direction)
            os.chdir(direction)
            print(f"Path: '{direction}' has been successfully created")
            return
        os.chdir(direction)


def create_file(file_name: list) -> None:
    with open(file_name[0], "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                print("Data recording is complete!")
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


if __name__ == "__main__":
    create_path(path)
    create_file(commands)
