import os
import sys
import datetime


def create_path() -> str:
    path = os.path.join(os.getcwd(), args[args.index("-d") + 1],
                 args[args.index("-d") + 2])
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> str:
    filename = args[args.index("-f") + 1]
    full_path = os.path.join(file_path, filename)
    with open(full_path, "w") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        count = 0
        string = ""
        while string != "stop":
            f.write(f"{count} " + string + "\n")
            count += 1
            string = input("Enter file name: ")
    return filename


args = sys.argv

if "-d" in args and "-f" in args:
    path = create_path()
    create_file(path)
elif "-d" in args:
    create_path()
else:
    create_file(os.getcwd())

