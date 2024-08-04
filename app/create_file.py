import os
import sys
from datetime import datetime


def path_handler(file_name: str | None, path: str | None) -> None:
    if path and not os.path.exists(path):
        os.makedirs(path)
    else:
        path = ""

    if file_name:
        with open(os.path.join(path, file_name), "a") as file:
            lines = []
            n_line = 1

            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                lines.append(f"{n_line} {line}\n")
                n_line += 1

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            file.write(f"{current_time}\n")
            file.writelines(lines)
            file.write("\n")


if __name__ == "__main__":
    args = sys.argv
    file_name = None
    path = None

    if "-d" in args:
        path = ""
        i = args.index("-d") + 1

        while i < len(args) and not args[i].startswith("-"):
            path = os.path.join(path, args[i])
            i += 1

    if "-f" in args:
        file_name = args[args.index("-f") + 1]

    path_handler(file_name, path)
