import os
import sys
import datetime


def create_file_from_terminal() -> None:
    console_init = sys.argv
    d_index = None
    f_index = None
    user_input = None

    if "-f" in console_init:
        f_index = console_init.index("-f")
    if "-d" in console_init:
        d_index = console_init.index("-d")

    if d_index is not None:
        if f_index is None:
            path = os.path.join(os.getcwd(), *console_init[d_index + 1:])
        if f_index is not None and f_index > d_index:
            path = os.path.join(
                os.getcwd(), *console_init[d_index + 1:f_index]
            )
        if f_index is not None and f_index < d_index:
            path = os.path.join(os.getcwd(), *console_init[d_index + 1:])
        os.makedirs(path, exist_ok=True)
    if f_index is not None:
        if d_index is None:
            file_path = console_init[f_index + 1]
        if d_index is not None:
            file_path = os.path.join(path, console_init[f_index + 1])

        with open(file_path, "a") as f:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                f.write("\n")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
            f.write(date)
            counter = 0
            while user_input != "stop":
                counter += 1
                user_input = input("Enter content line: ")
                if user_input != "stop":
                    f.write(f"{counter} {user_input}\n")


create_file_from_terminal()
