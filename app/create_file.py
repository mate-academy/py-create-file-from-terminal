import os
import sys
from datetime import datetime


def create_file() -> None:
    current_dir = os.getcwd()
    if "-d" in sys.argv and "-f" in sys.argv:
        for i in range(sys.argv.index("-d"), sys.argv.index("f")):
            name_dir = os.path.join(current_dir, sys.argv[i])
            os.makedirs(name_dir)

    elif "-d" in sys.argv:
        for i in range(sys.argv.index("-d")):
            name_dir = os.path.join(current_dir, sys.argv[i])
            os.makedirs(name_dir)

    if "-f" in sys.argv:
        data_current = datetime.now()
        file_line = ""
        index_line = 1

        with open(str(sys.argv[sys.argv.index("-f") + 1]), "a") as f:
            f.write(f"{data_current.strftime('%Y')}-"
                    f"{data_current.strftime('%m')}-"
                    f"{data_current.strftime('%d')}-"
                    f"{data_current.strftime('%H')}-"
                    f"{data_current.strftime('%M')}-"
                    f"{data_current.strftime('%S')}-")

            while file_line != "stop":
                file_line = input("Enter content line: ")
                if file_line == "stop":
                    break
                f.write(f"{index_line}, {file_line}\n")
                index_line += 1
