import os
import sys
from datetime import datetime


def create_file(name_of_file: str) -> None:
    if os.path.exists(name_of_file):
        pass
        # with open(name_of_file, "w", open(name_of_file, "r") as new_file:
        #     new_file.write(new_file.readline())
        #     while True:
        #         new_content = input("Enter new content line (or stop): ")
        #         if new_content == "stop":
        #             break

    with open(name_of_file, "a") as new_file:
        today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(today)
        iteration = 1
        while True:
            content = input("Enter content line (or stop): ")
            if content == "stop":
                break
            new_file.write(f"\n{iteration} " + content)
            iteration += 1
    with open(name_of_file, "r") as new_file:
        print(f"Content in this file now:\n\n{new_file.read()}")


def create_directory(*name_of_directory: list) -> None:
    os.makedirs(os.path.join(*name_of_directory))


def operations_with_command():
    while True:
        commands = list(input("Enter your command (use -b or/and -f) or exit: ").split())

        if "-d" in commands and "-f" not in commands:
            # create_directory(commands[3:])
            create_directory(*commands[commands.index("-d") + 1:])  # змінено передачу аргументів
            break
        elif "-d" not in commands and "-f" in commands:
            create_file(commands[-1])
            break
        elif "-d" in commands and "-f" in commands:
            # create_directory()
            # create_file()
            ...
        elif commands == "exit":
            print("Exiting proses.. ")
            break
        else:
            print("Command not found")


if __name__ == "__main__":
    operations_with_command()
    # create_file("file1.txt")
