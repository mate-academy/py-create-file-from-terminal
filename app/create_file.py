import os
import sys


def create_file(lines: str) -> None:
    user_text = input(f"Enter content line: {lines}")
    with open("user_text", "w") as file:
        direct_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")
        start = sys.argv.index("-d")
        end = sys.argv.index("-f")

        if "-d" and "-f" in sys.argv:
            for i in range(start, end):
                if i != "stop":
                    direct_name = sys.argv[direct_index + i]
                    if direct_name != file_index:
                        os.makedirs(direct_name)
                else:
                    break
            for i in range(end, len(sys.argv)):
                if i != "stop":
                    file_name = sys.argv[file_index + i]
                    with open(file_name, "w") as name_file:
                        name_file.write(user_text)
                else:
                    break

        if "-d" in sys.argv :
            for i in range(start, end):
                if i != "stop":
                    direct_name = sys.argv[direct_index + i]
                    if direct_name != file_index:
                        os.makedirs(direct_name)
                else:
                    break

        if "-f" in sys.argv:
            for i in range(end, len(sys.argv)):
                if i != "stop":
                    file_name = sys.argv[file_index + i]
                    with open(file_name, "w") as name_file:
                        name_file.write(user_text)
                else:
                    break
    file.write(user_text)
