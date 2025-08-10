import sys
import os
import datetime


def create_file() -> None:
    enter = sys.argv
    path = ""

    if "-d" in enter:
        path = os.path.join(*enter[2: -2])
        os.makedirs(path)

    if "-f" in enter:
        with open(rf"{path}\{enter[-1]}", "a") as f:
            f.write(
                f"{datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S' )}\n"
            )
            line_counter = 0

            while True:
                line_counter += 1
                user_input = input("Enter content line: ")
                if user_input == "stop":
                    f.write("\n")
                    break
                f.write(f"{line_counter} {user_input}\n")


if __name__ == "__main__":
    create_file()
