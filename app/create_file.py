import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    current_flag = None
    dirs = []
    filename = None
    for arg in args:
        if arg in ["-d", "-f"]:
            current_flag = arg
            continue
        if current_flag == "-d":
            dirs.append(arg)
        elif current_flag == "-f":
            filename = arg

    dirpath = ""
    if dirs:
        for directory in dirs:
            dirpath = f"{dirpath}{directory}/"
            if not os.path.exists(dirpath):
                os.mkdir(dirpath)

    if not filename:
        return

    filepath = f"{dirpath}{filename}"
    with open(filepath, "a+") as file:
        has_content = os.path.getsize(filepath) > 0
        if has_content:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        index = 0
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            index += 1
            file.write(f"{index} {content}\n")


main()
