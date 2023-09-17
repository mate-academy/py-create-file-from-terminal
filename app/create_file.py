import sys
import os
import datetime


def write_into_file(path: str) -> None:
    with open(path, "a") as file:
        count_of_lines = 0
        file.write(str(current_day.strptime(
            current_day.strftime("%I:%M%p %d/%B/%Y"),
            "%I:%M%p %d/%B/%Y")) + "\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            else:
                file.write(str(count_of_lines) + " " + line + "\n")
                count_of_lines += 1


def make_dirs(path: str) -> None:
    os.makedirs(path)


def ask_for_path() -> str:
    name_dirs = input("Enter name of the dir ")
    name_dirs_list = name_dirs.split(" ")
    return "app\\" + "\\".join(name_dirs_list)


current_day = datetime.datetime.now()
if "-d" in sys.argv and "-f" not in sys.argv:
    path = ask_for_path()
    make_dirs(path)
elif "-f" in sys.argv and "-d" not in sys.argv:
    write_into_file("app\\file.txt")
else:
    path = ask_for_path()
    make_dirs(path)
    write_into_file(path + "\\file.txt")
