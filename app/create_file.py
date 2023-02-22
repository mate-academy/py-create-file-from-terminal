import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-f')
parser.add_argument('-d', nargs="*")
arguments = vars(parser.parse_args())


def create_file(path: str) -> None:
    with open(path, "a+") as file:
        file.write(datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "\n")
        line_counter = 1
        while True:
            content = input("Enter content line:")
            if content == "stop":
                file.write("\n")
                break
            file.write(f"{line_counter} {content}" "\n")


if arguments.get("d") and arguments.get("f"):

    os.makedirs(os.path.join(*arguments["d"]), exist_ok=True)
    create_file(os.path.join(*arguments["d"], arguments["f"]))

elif arguments.get("d"):
    os.makedirs(os.path.join(*arguments["d"]), exist_ok=True)

elif arguments.get("f"):
    create_file(arguments["f"])
