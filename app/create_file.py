import sys
import datetime
import os


def file_input() -> None:
    time_now = datetime.datetime.now()
    if "-d" in sys.argv:
        for arg in (2, sys.argv):
            if "-f" not in sys.argv[arg]:
                os.makedirs(sys.argv[arg])
                break

    if "-f" in sys.argv:
        with open(sys.argv[-1], "a") as file:
            text = file.write(f"{time_now.strftime('%m/%d/%Y, %H:%M:%S')}\n")
            line = 1

            while True:
                content_input = input("Enter content line: ")
                if content_input != "stop":
                    file.write(f"{line} {text}\n")
                    line += 1
                    break
                file.write("\n")
