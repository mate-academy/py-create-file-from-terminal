import os
import sys


def create_file(lines: str) -> None:
    user_text = input(f"Enter content line: {lines}")

    direct_index = sys.argv.index("-d")
    file_index = sys.argv.index("-f")

    if "-d" in sys.argv :
        for i in range(direct_index, file_index):
            if sys.argv[i] != "stop":
                if sys.argv[i] != "-f":
                    os.makedirs(sys.argv[i])
            else:
                break

    if "-f" in sys.argv:
        for i in range(file_index, len(sys.argv)):
            if sys.argv[i] != "stop":
                with open(sys.argv[i], "w") as name_file:
                    name_file.write(user_text)
            else:
                break
