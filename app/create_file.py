import sys
import os
import datetime


def create_file():
    user_enter = sys.argv
    path = ""

    if "-d" in user_enter:
        path = os.path.join(*user_enter[(user_enter.index("-d") + 1):user_enter.index("-f")])
        if os.path.exists(f"{path}\{user_enter[-1]}") is False:
            os.makedirs(path)

    with open(f"{path}\{user_enter[-1]}", "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S' )}\n")
        line_counter = 0
        while True:
            line_counter += 1
            user_input = input("Enter content line: ")
            if user_input != "stop":
                f.write(f"{line_counter} {user_input}\n")
            else:
                break


create_file()
