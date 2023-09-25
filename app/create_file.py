import sys
import os
from datetime import datetime


def create_directories(directories: list) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_path: str) -> None:
    if not os.path.exists(file_path):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a") as file:
            file.write(f"{current_time}\n")

        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                with open(file_path, "a") as file:
                    file.write("\n")
                break
            with open(file_path, "a") as file:
                file.write(f"{line} {content}\n")
            line += 1
    else:
        print(f"'{file_path}' already exists.")


def main():
    command = sys.argv

    if "-d" in command and "-f" in command:
        start = command.index("-d") + 1
        end = command.index("-f")

        path_to_file = create_directories(command[start:end])
        create_file(os.path.join(path_to_file, command[end + 1]))

    elif "-d" in command:
        start = command.index("-d") + 1
        end = len(command)
        create_directories(command[start:end])

    elif "-f" in command:
        index = command.index("-f") + 1
        create_file(command[index])


if __name__ == "__main__":
    main()
