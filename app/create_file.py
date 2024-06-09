import sys
import os
import datetime


def get_command() -> None:
    if "-f" in commamd:
        create_file()
    if "-d" in commamd and "-f" not in commamd:
        directory = os.path.join(*commamd[commamd.index("-d") + 1:])
        os.makedirs(directory, exist_ok=True)


def create_file() -> None:
    f_ind = commamd.index("-f")
    file_name = commamd[-1]
    directory = ""
    if "-d" in commamd:
        directory = os.path.join(*commamd[commamd.index("-d") + 1: f_ind])
        os.makedirs(directory, exist_ok=True)
    mode = "a" if os.path.exists(directory + file_name) else "w"
    with open(directory + file_name, mode) as file:
        file.write(
            f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
        )
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{text}\n")


commamd = sys.argv
if __name__ == "__main__":
    # commamd = ["create_file.py", "-d", "dir1", "dir2", "-f", "file.txt"]
    get_command()
