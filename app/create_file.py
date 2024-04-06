import sys
import os
from datetime import datetime


def time_code() -> str:
    return datetime.now().strftime("%Y-%m-%d, %H:%M:%S")


def write_to_file(work_file: open) -> None:
    work_file.write(f"{time_code()}\n")
    num_line = 1
    while True:
        input_text = input("Enter content line: ")
        if input_text == "stop":
            break
        work_file.write(f"{num_line} {input_text}\n")
        num_line += 1


def command_input() -> None:
    for line in sys.stdin:
        line = line.rstrip()
        if "-d" == line[0:2] and "-f " in line:
            path = os.path.join(*line[3:line.index("-f ")].split())
            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path,
                                   line[line.index("-f ") + 3:]),
                      "a") as file:
                write_to_file(file)
            break
        elif "-d" == line[0:2]:
            path = os.path.join(*line[3:].split())
            os.makedirs(path, exist_ok=True)
            break
        elif "-f" == line[0:2]:
            with open(line[3:], "a") as file:
                write_to_file(file)
            break


if __name__ == "__main__":
    command_input()
