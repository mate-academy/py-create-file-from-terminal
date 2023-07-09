import os
import sys
from datetime import datetime


def file_input() -> None:
    time_now = datetime.now()
    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory_path = os.path.join(*sys.argv[directory_index:])
        os.makedirs(directory_path, exist_ok=True)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        with open(file_name, "a") as file:
            file.write(f"{time_now.strftime('%m/%d/%Y, %H:%M:%S')}\n")
            line = 1
            while True:
                content_input = input("Enter content line: ")
                if content_input != "stop":
                    file.write(f"{line} {content_input}\n")
                    line += 1
                else:
                    break
