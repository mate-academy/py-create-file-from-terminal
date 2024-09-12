import sys
import os
import datetime


def create_path() -> None:
    command = sys.argv
    if command[1] == "-d":
        if "-f" not in command:
            path = os.path.join("/".join(command[2:]))
            create_dir(path)
        else:
            path = os.path.join("/".join(command[2:command.index("-f")]))
            create_dir(path)
            os.chdir(path)
            create_file("file.txt")
    elif command[1] == "-f":
        file_name = command[2]
        if "-d" not in command:
            create_file(file_name)
        else:
            path = os.path.join("/".join(command[command.index("-d") + 1:]))
            create_dir(path)
            os.chdir(path)
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
                file.write("\n")
                break
            file.write(f"{count} " + content + "\n")
            count += 1


if __name__ == "__main__":
    create_path()