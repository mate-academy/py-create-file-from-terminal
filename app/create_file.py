import os
import sys
from datetime import datetime


def create_path(path: str) -> None:
    file_path = path.strip().split("-d")[-1].strip().split()
    full_path = os.path.join(*[os.getcwd(), *file_path])
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return


def create_file(command: list[str]) -> None:
    command = " ".join(command)
    file_name = None
    full_path = None
    if "-f" in command:
        file_name = command.strip().split("-f")[1].strip()
        full_path = file_name

    if "-d" in command and "-f" in command:
        file_path = command.strip(

        ).split("-f")[0].split("-d")[-1].strip().split()
        full_path = os.path.join(*[os.getcwd(), *file_path, file_name])
        create_path(os.path.join(os.getcwd(), *file_path))

    if full_path is None:
        if "-d" in command:
            create_path(command)
            return

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


if __name__ == "__main__":
    create_file(sys.argv)
