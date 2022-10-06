import datetime
import os
import sys


def create_file() -> None:
    entered_info = sys.argv
    path = ""

    if "-d" in entered_info:
        path = os.path.join(
            *entered_info[
                (entered_info.index("-d") + 1):entered_info.index("-f")
            ]
        )
        if not os.path.exists(f"{path}\\{entered_info[-1]}"):
            os.makedirs(path)

    with open(f"{path}\\{entered_info[-1]}", "a") as result:
        data_inf = f"{datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n"
        result.write(data_inf)

        count = 0

        while True:
            text_input = input("Enter content line: ")
            count += 1
            if text_input == "stop":
                break
            else:
                result.write(f"{count} {text_input}\n")
