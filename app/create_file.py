# write your code here
from datetime import datetime
import sys
import os


def create_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as file:
        file.write(str(datetime.now().
                       strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        line = 0
        while True:
            content = input("Enter content line: ")
            line += 1
            if content == "stop":
                break
            file.write(f"{line} " + content + "\n")
        file.write("\n")


def main() -> None:
    args = sys.argv
    to_dir = ""

    if args[1] == "-d":
        to_dir = (os.path.join(*args[2:]) if "-f" not in args else
                  os.path.join(*args[args.index("-d") + 1:args.index("-f")]))
        os.makedirs(to_dir, exist_ok=True)

    if "-f" in args:
        to_file = os.path.join(to_dir, args[args.index("-f") + 1])
        create_file(to_file)


if __name__ == "__main__":
    main()
