import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        directory = os.path.join(*args[dir_index + 1:file_index])
        filename = args[file_index + 1]
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_join = os.path.join(directory, filename)
        if os.path.exists(directory):
            create_file(file_join)
    elif "-d" in args:
        directory = os.path.join(*args[args.index("-d") + 1:])
        os.makedirs(directory)
    elif "-f" in args:
        filename = args[args.index("-f") + 1]
        create_file(filename)
    else:
        print("Invalid arguments")
        return


def create_file(filename: str) -> None:
    with open(filename, "a") as file, open(filename, "r") as read_file:
        if read_file.read() != "":
            file.write("\n\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        line_number = 1
        lines = []
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            lines.append(f"{line_number} {line}")
            line_number += 1
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
