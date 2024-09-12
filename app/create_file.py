import sys
import os
import datetime


def create_path() -> None:
    command = sys.argv
    if "-d" in command:
        if "-f" not in command:
            path = os.path.join("/".join(command[command.index("-d") + 1:]))
            create_dir(path)
        else:
            path = os.path.join("/".join(
                command[command.index("-d") + 1:command.index("-f")]))
            create_dir(path)
            os.chdir(path)
            create_file("file.txt")
    elif "-f" in command:
        file_name = command[command.index("-f") + 1]
        create_file(file_name)


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        current_date = datetime.datetime.now()
        file.write(current_date.strftime("%Y-%d-%m %H:%M:%S") + "\n")
        while True:
            content = input("Enter content line: ")
            count = 1
            if content == "stop":
                break
            file.write(f"{count} " + content + "\n")
            count += 1


if __name__ == "__main__":
    create_path()
