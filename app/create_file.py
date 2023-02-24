from datetime import datetime
import sys
import os


def create_derectory() -> None:
    current = os.getcwd()
    command = sys.argv
    command_f = "-f"
    command_d = "-d"
    if command_d in command:
        for line in range(2, len(command)):
            if command[line] == command_f:
                break
            current = os.path.join(current, command[line])
        os.mkdir(current)


def create_file(file_name: str) -> None:
    with open(file_name, "w") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_counter = 1
        while True:
            asker = input("Enter content line: ")
            if asker == "stop":
                break
            new_file.write(f"{line_counter} {asker}")
            line_counter += 1


if __name__ == "__main__":
    create_file("hello.txt")
    create_derectory()
