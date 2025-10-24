import os
from datetime import datetime
import sys


def write_text(file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
        all_text = []
        while True:
            text = input("Enter content line:")
            if text.lower() == "stop":
                break
            all_text.append(text)

        for index, line in enumerate(all_text, start=1):
            file.write(f"{index} {line}\n")


start = sys.argv[1:]
if "-d" in start and "-f" in start:
    d_index = start.index("-d")
    f_index = start.index("-f")

    file_name = start[f_index + 1]
    dirs = start[d_index + 1 : f_index]

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, file_name)
    write_text(file_path)
elif "-d" in start:
    d_index = start.index("-d")
    dirs = start[d_index + 1:]
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
elif "-f" in start:
    f_index = start.index("-f")
    file_name = start[f_index + 1]
    file_path = os.path.join(os.getcwd(), file_name)
    write_text(file_path)
