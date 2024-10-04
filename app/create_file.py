import os
import sys
from datetime import datetime


is_first_entry = True


def create_directory(way: list) -> None:
    if "-f" in way:
        way.remove("-f")
        path = os.path.join(*way[:-1])
        try:
            os.makedirs(path)
        except Exception:
            pass
        current_path = os.path.join(*way)
        create_file(current_path)
        return

    path = os.path.join(*way)
    os.makedirs(path)


def create_file(way: str) -> None:
    with open(way, "a") as new_file:
        with open(way, "r") as read_file:
            if len(str(read_file.read())) != 0:
                global is_first_entry
                is_first_entry = False

        if not is_first_entry:
            new_file.write("\n")
        new_file.write(
            str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n"
        )
        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            new_file.write(f"{str(count)} " + line + "\n")
            count += 1


current_directory, flag, *expected_way = sys.argv

if flag == "-d":
    create_directory(expected_way)
if flag == "-f":
    create_file(*expected_way)
