from datetime import datetime
import sys
import os


def create_file(file_name: str) -> None:
    line_number = 1
    text = ""

    while True:
        content = input("Enter content line:")
        if content == "stop":
            break
        text += f"{line_number} {content}\n"
        line_number += 1

    with open(file_name, "a") as file:
        date_time = datetime.now().strftime("%Y %m %d %H:%M:%S")
        file.write(f"{date_time}\n{text}")


def create_folder() -> None:
    command = sys.argv
    if "-d" in command and "-f" in command:
        folders = os.path.join(*command[2:command.index("-f")])
        os.makedirs(folders)
        create_file(os.path.join(folders, command[-1]))

    elif "-d" in command and len(sys.argv) > 2:
        folders = os.path.join(*command[2:])
        os.makedirs(folders)

    elif "-f" in command and len(sys.argv) > 2:
        create_file(command[-1])


if __name__ == "__main__":
    create_folder()
