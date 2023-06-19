import os
import sys
from datetime import datetime


def create_file() -> None:
    command = sys.argv
    if "-f" in command:
        file_name = command[-1]
        if "-d" in command:
            dir_list = command[command.index("-d") + 1 : command.index("-f")]
            path = os.path.join(*dir_list)
            os.makedirs(path, exist_ok=True)
            file_name = f"{path}/{file_name}"
        with open(file_name, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            line = 0
            while True:
                content = input("Enter content line:")
                if content == "stop":
                    file.write("\n")
                    break
                line += 1
                file.write(f"{line} {content} \n")

    elif "-d" in command:
        dir_list = command[command.index("-d") + 1:]
        path = os.path.join(*dir_list)
        os.makedirs(path, exist_ok=True)


if __name__ == "__main__":
    create_file()
