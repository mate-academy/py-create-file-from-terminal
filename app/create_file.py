import sys
import os
from datetime import datetime


def create_file() -> None:
    command = sys.argv

    if "-d" in command:
        path_new = []
        for commands in command[command.index("-d") + 1:]:
            if commands == "-f":
                break
            else:
                path_new.append(commands)
        os.makedirs(os.path.join(*path_new), exist_ok=True)
        os.chdir(os.path.join(*path_new))

    if "-f" in command:
        with open(command[-1], "w") as file:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{date}\n")
            line = 1
            content = input("Enter content line: ")
            while content != "stop":
                file.write(f"Line{line} {content}")
                content = input("Enter content line: ")
                line += 1


if __name__ == "__main__":
    create_file()
