import sys
import os
import datetime

commands = sys.argv[1:]
file_name = " ".join(commands).split("-f")
print(file_name)
path = file_name.pop(0).strip("-d").split()


def create_path(direction: list) -> None:
    if direction:
        direction = os.path.join(*direction)
        if not os.path.exists(direction) and len(direction) > 0:
            os.makedirs(direction)
            print(f"Path: '{direction}' has been successfully created")
        os.chdir(direction)


def create_file(name: list) -> None:
    with open(name[0], "a") as file:
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
    create_file(file_name)
