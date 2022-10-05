import sys
import os
import datetime


def create_file() -> None:
    enter = sys.argv
    path = ""

    if "-d" in enter:
        path = os.path.join(*enter[(enter.index("-d") + 1):enter.index("-f")])
        if os.path.exists(rf"{path}\{enter[-1]}") is False:
            os.makedirs(path)

    with open(rf"{path}\{enter[-1]}", "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S' )}\n")
        line_counter = 0
        while True:
            line_counter += 1
            user_input = input("Enter content line: ")
            if user_input != "stop":
                f.write(f"{line_counter} {user_input}\n")
            else:
                f.write("\n")
                break


create_file()
