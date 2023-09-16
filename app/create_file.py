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


def make_dirs() -> None:
    os.makedirs("app/dir1/dir2")


current_day = datetime.datetime.now()
if "-d" in sys.argv and "-f" not in sys.argv:
    make_dirs()


elif "-f" in sys.argv and "-d" not in sys.argv:
    write_into_file("app\\file.txt")
else:
    make_dirs()
    write_into_file("app\\dir1\\dir2\\file.txt")
