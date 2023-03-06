import os
import sys
from datetime import datetime


COMMAND = sys.argv
CHECK_D = "-d"
CHECK_F = "-f"


def create_from_terminal() -> None:
    path = ""

    if CHECK_D in COMMAND:
        current_dir = sys.argv.index(CHECK_D) + 1
        path = os.path.join(*COMMAND[current_dir:])
        if CHECK_F in COMMAND:
            path = path.split(CHECK_F)[0]
        os.makedirs(path, exist_ok=True)

    if CHECK_F in COMMAND:
        current_file = COMMAND.index(CHECK_F) + 1
        file_path = path + COMMAND[current_file]
        with open(file_path, "a") as new_file:
            line_counter = 1
            new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            while True:
                asker = input("Enter content line: ")
                if asker == "stop":
                    break
                new_file.write(f"{line_counter}: {asker}")
                line_counter += 1
                new_file.write("\n")


if __name__ == "__main__":
    create_from_terminal()
