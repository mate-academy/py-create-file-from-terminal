import sys
from datetime import datetime
import os


def write_content(file_name: str) -> None:
    with open(file_name, "a") as file:
        if file.tell() > 0:
            file.write("\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        count = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{count} {text}\n")
            count += 1


def create_file() -> None:
    if len(sys.argv) == 1:
        return
    if sys.argv[1] == "-f" and "-d" not in sys.argv:
        file_name = sys.argv[2]
        write_content(file_name)
        return
    if sys.argv[1] == "-d" and "-f" not in sys.argv:
        real_path = ""
        for path in sys.argv[2:]:
            real_path = os.path.join(real_path, path)
        os.makedirs(real_path)
        return

    index_d = sys.argv.index("-d")
    index_f = sys.argv.index("-f")
    real_path = ""
    if index_d < index_f:
        for i in range(index_d + 1, index_f):
            real_path = os.path.join(real_path, sys.argv[i])
        if not os.path.exists(real_path):
            os.makedirs(real_path)
        file_name = sys.argv[index_f + 1]
        real_path = os.path.join(real_path, file_name)
        write_content(real_path)
    else:
        for i in range(index_d + 1, len(sys.argv)):
            real_path = os.path.join(real_path, sys.argv[i])
        if not os.path.exists(real_path):
            os.makedirs(real_path)
        file_name = sys.argv[index_f + 1]
        real_path = os.path.join(real_path, file_name)
        write_content(real_path)


create_file()
