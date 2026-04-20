import sys
import os
from datetime import datetime


def create_dirs(cwd: str, *dirs) -> str:
    path = os.path.join(cwd, *dirs)

    if not os.path.exists(path):
        os.makedirs(path)

    return path


def create_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 0
        while True:
            line = input("Enter a new line: ")
            line_number += 1

            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")

        file.write("\n")


def main() -> None:
    command = sys.argv
    cwd = os.getcwd()

    if "-d" in command:
        if "-f" not in command:
            create_dirs(cwd, *command[2:])

            return
        else:
            path = create_dirs(cwd, *command[2:-2])
            new_path = f"{os.path.join(path, command[-1])}"

            create_file(new_path)

            return

    if "-f" in command:
        create_file(f"{os.path.join(command[-1])}")


if __name__ == "__main__":
    main()
