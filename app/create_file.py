import os
import sys

from datetime import datetime


def create_file() -> None:
    if "-d" in sys.argv:
        dir_path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        os.makedirs(dir_path, exist_ok=True)
    if "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        if os.path.isfile(file_name):
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(file_name, "a") as f:
                f.write(f"{time_now}\n")
                line = 1
                while True:
                    content = input("Enter content line: ")
                    if content == "stop":
                        f.write("\n")
                        break
                    f.write(f"{line} {content}\n")
                    line += 1
        else:
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(file_name, "w") as f:
                f.write(f"{time_now}\n")
                line = 1
                while True:
                    content = input("Enter content line: ")
                    if content == "stop":
                        f.write("\n")
                        break
                    f.write(f"{line} {content}\n")
                    line += 1


print(create_file())
