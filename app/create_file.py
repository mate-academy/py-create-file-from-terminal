import os
import sys
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
        if os.path.exists(file_name):
            open(file_path, "a").write("\n")
        with open(file_path, "a", newline="\n") as file:
            line_number = 1
            now = datetime.datetime.now()
            file.write(f"{now.strftime("%Y-%m-%d %H:%M:%S")}\n")
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                file.write(f"{line_number} {text}\n")
                line_number += 1


if __name__ == "__main__":
    create_file(sys.argv[1:])
