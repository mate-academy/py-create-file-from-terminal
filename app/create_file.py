from datetime import datetime
import sys
import os


def create_directory() -> None:
    command = sys.argv
    if "-d" in command:
        for line in range(2, len(command)):
            if command[line] == "-f":
                break
            current = os.path.join(os.getcwd(), command[line])
            os.makedirs(current, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "w") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_counter = 1
        while True:
            asker = input("Enter content line: ")
            if asker == "stop":
                new_file.write("\n")
                break
            new_file.write(f"{line_counter} {asker}")
            line_counter += 1
