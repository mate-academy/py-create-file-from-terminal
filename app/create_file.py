import os
import sys
from datetime import datetime


def create_directory(command: list[str]) -> str:
    path = "./"
    for value in command[command.index("-d") + 1:]:
        if value == "-f":
            break

        path += f"{value}/"

    os.makedirs(path, exist_ok=True)
    return path


def create_file(path: str, filename: str) -> None:
    full_path = f"{path}/{filename}"

    if not os.path.exists(full_path):
        is_new_file = True
    else:
        is_new_file = False

    with open(full_path, "a") as file:
        if not is_new_file:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        i = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break

            file.write(f"{i} {new_line}\n")
            i += 1


def main() -> None:
    if len(sys.argv) < 3:
        return

    command = sys.argv[1:]

    full_path = "./"
    if "-d" in command:
        full_path = create_directory(command)

    if "-f" in command:
        create_file(
            full_path,
            command[command.index("-f") + 1]
        )


main()
