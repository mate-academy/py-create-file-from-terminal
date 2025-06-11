import datetime
import os
import sys


dir_path = []
filename = None


if "-d" in sys.argv:
    index_d = sys.argv.index("-d")

    if "-f" in sys.argv:
        index_f = sys.argv.index("-f")
        dir_path = sys.argv[index_d + 1 : index_f]

    else:
        dir_path = sys.argv[index_d + 1:]

if "-f" in sys.argv:
    index_f = sys.argv.index("-f")
    filename = sys.argv[index_f + 1]

dir_path = os.path.join(*dir_path) if dir_path else "."
file_path = os.path.join(dir_path, filename)


def current_time() -> str:
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time


def write_to_file() -> None:
    line = ""
    os.makedirs(dir_path, exist_ok=True)

    with open(file_path, "a") as f:
        f.write(current_time() + "\n")

        while True:
            line = str(input("Enter content line: "))
            if line.lower() == "stop":
                break
            f.write(line + "\n")
