import sys
import os
import datetime


def command_name() -> None:
    if "-d" in commamd and "-f" not in commamd:
        path_info = os.path.join(*commamd[commamd.index("-d") + 1:])
        create_directory(path_dest)
    if "-d" in commamd and "-f" in commamd:
        path_dest = os.path.join(
            *commamd[commamd.index("-d") + 1:commamd.index("-f")])
        create_directory(path_info)
        create_file(path_info)
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
    command_name()