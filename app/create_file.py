import sys
import os
from datetime import datetime

home_directory = sys.argv


def command_d() -> None:
    if "-d" in home_directory and "-f" not in home_directory:
        file_path = "\\".join(home_directory[home_directory.index("-d") + 1::])
        path = os.path.join(file_path)
        os.makedirs(path)


def command_f() -> None:
    count = 0
    if "-f" in home_directory and "-d" not in home_directory:
        with open(home_directory[home_directory.index("-f") + 1], "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                count += 1
                word = input("Enter content line:")
                if word == "stop":
                    break
                file.write(f"{count} {word}\n")


def command_d_and_f() -> None:
    if "-d" in home_directory and "-f" in home_directory:
        file_path = "\\".join(
            home_directory[home_directory.index("-d") + 1:
                           home_directory.index("-f")]
        )
        path = os.path.join(file_path)
        os.makedirs(path)
        count = 0
        path += "\\" + home_directory[home_directory.index("-f") + 1]
        with open(path, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                count += 1
                word = input("Enter content line:")
                if word == "stop":
                    break
                file.write(f"{count} {word}\n")


if __name__ == "__main__":
    command_f()
    command_d_and_f()
    command_d()
