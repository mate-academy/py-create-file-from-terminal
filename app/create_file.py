import os
import datetime


def create_file(args: list[str]) -> None:
    dirs = []
    if "-d" in args:
        start = args.index("-d") + 1
        end = args.index("-f") \
            if "-f" in args and args.index("-f") > start\
            else len(args)
        dirs = args[start:end]

    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)

    file_name = ""

    if "-f" in args:
        file_name = args[args.index("-f") + 1]

    if file_name:
        file_path = os.path.join(*dirs, file_name)

        with open(file_path, "a", newline="\n") as f:
            line_number = 1
            f.write(f"{str(datetime.datetime.today())[:19]}\n")
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    f.write("\n")
                    break
                f.write(f"{line_number} {text}\n")
                line_number += 1
