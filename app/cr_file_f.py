import sys
import os
import datetime


def create_file(path: str = None) -> None:
    with open(path, "a") as f:
        print("Input content lines.\n"
              "Type 'stop' to finish entering content.\n"
              )
        start_log_time = datetime.datetime.now()
        f.write(f"{start_log_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            user_input = input(">>>   ")
            if user_input.lower() != "stop":
                f.write(f"{user_input}\n")
            else:
                f.write("\n")
                break