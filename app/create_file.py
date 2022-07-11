import sys
import os
from datetime import datetime


def create_file(command: list):
    path = None
    file_name = None
    if "-d" in command and "-f" in command:
        for i in range(len(command)):
            if command[i] == "-d":
                path = command[i + 1:]
            if command[i] == "-f":
                path = "/".join(path[:i - 2])
                file_name = path + "/" + command[-1]
                os.makedirs(path)
                break
    elif "-d" in command:
        for i in range(len(command)):
            if command[i] == "-d":
                path = "/".join(command[i + 1:])
                os.makedirs(path)
    elif "-f" in command:
        file_name = command[-1]

    if "-f" in command:
        with open(file_name, "a") as new_file:
            new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            line = 1
            while True:
                input_text = input("Enter content line: ")
                new_file.write(f"{line} {input_text} \n")
                line += 1

                if input_text == "stop":
                    break


if __name__ == "__main__":
    create_file(sys.argv)
