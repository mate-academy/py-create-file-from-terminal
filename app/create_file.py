import os
import sys
from datetime import datetime


def create_file_from_terminal(command: str) -> None:
    full_path = None
    if "-d" in command and "-f" in command:
        file_path = command.strip(

        ).split("-f")[0].split("-d")[-1].strip().split()
        file_name = command.strip().split("-f")[1].strip()
        full_path = os.path.join(*[os.getcwd(), *file_path, file_name])

    elif "-d" in command:
        file_path = command.strip().split("-d")[-1].strip().split()
        full_path = os.path.join(*[os.getcwd(), *file_path])
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        return

    elif "-f" in command:
        file_name = command.strip().split("-f")[1]
        full_path = file_name

    mode = "a" if os.path.exists(full_path) else "w"

    with open(full_path, mode) as file:
        file.write(datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        line_char = 0
        while True:
            line_char += 1
            input_data = str((input("Enter content line: ")))
            if input_data == "stop":
                break
            file.write(f"{line_char} {input_data}\n")
        file.write("\n")


create_file_from_terminal(sys.argv[1])
