import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv
    if "-d" in args:
        for i in args[2:]:
            os.mkdir(i)
    elif "-f" in args:
        name = " ".join(args[2:])
        with open(name, "a") as file:
            time_head = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(time_head + "\n")
            num = 0
            while True:
                num += 1
                command = input("Enter content line: ")
                if command.lower() == "stop":
                    break
                else:
                    file.write(f"{num} {command}\n")


if __name__ == "__main__":
    main()
