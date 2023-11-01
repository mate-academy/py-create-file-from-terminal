import os
import sys
from datetime import datetime


def parse_dir_file(args: list[str]) -> str:
    file_name = ""
    dir_path = ""
    if len(args) >= 3 and args[1] == "-d":
        for i in range(2, len(args)):
            if args[i] == "-f":
                if (i + 1) <= (len(args) - 1):
                    file_name = args[i + 1]
                    print("file_name = ", file_name)
                break

            dir_path = os.path.join(dir_path, args[i])

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    elif len(args) >= 3 and args[1] == "-f":
        file_name = args[2]

    if dir_path:
        file_name = os.path.join(dir_path, file_name)

    return file_name


def creat_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        date = datetime.now()
        f.write(date.strftime("%Y-%m-%d %H:%M:%S\n"))
        text = input("Enter content line:")
        is_stop = text.lower()
        coгnter = 1
        while is_stop != "stop":
            f.write(f"{str(coгnter)}. {text}\n")
            text = input("Enter content line:")
            coгnter += 1
            is_stop = text.lower()


file_name = parse_dir_file(sys.argv)

if file_name:
    creat_file(file_name)
