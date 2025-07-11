import sys
import datetime
import os
from typing import Any


def create_file() -> Any:
    arguments = sys.argv
    dir_path = ""
    file_name = ""

    try:
        if "-d" in arguments:
            flag_d = arguments.index("-d")
            next_flag = arguments.index("-f")\
                if "-f" in arguments\
                else len(arguments)
            dir_path = "/".join(arguments[flag_d + 1 : next_flag])
            os.makedirs(dir_path, exist_ok=True)

        if "-f" in arguments:
            flag_f = arguments.index("-f")
            file_name = arguments[flag_f + 1]

        file_path = f"{dir_path}/{file_name}" if dir_path else file_name

        with open(file_path, "a") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n{timestamp}\n")
            while True:
                line = input("Input ")
                if line.strip().lower() == "stop":
                    break
                f.write(line + "\n")
    except Exception as e:
        print(f"Error: {e}")


create_file()
