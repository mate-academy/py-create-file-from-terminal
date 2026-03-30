import sys
import os
import datetime


def get_command() -> None:
    if "-d" in commamd and "-f" not in commamd:
        path_dest = os.path.join(*commamd[commamd.index("-d") + 1:])
        create_directory(path_dest)
    if "-d" in commamd and "-f" in commamd:
        index_f = commamd.index("-f")
        path_dest = os.path.join(*commamd[commamd.index("-d") + 1:index_f])
        create_directory(path_dest)
        create_file(path_dest)
    if "-f" in commamd and "-d" not in commamd:
        create_file("")


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(path: str) -> None:
    path = os.path.join(path, commamd[-1])
    mode = "a" if os.path.exists(path) else "w"
    write_to_file(path, mode)


def write_to_file(path_file: str, mode: str) -> None:
    with open(path_file, mode) as file:
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
    get_command()
