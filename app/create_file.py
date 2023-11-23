import sys
import os

from datetime import datetime


def make_dir(command: list) -> None:
    full_path = os.path.join(*command)

    if full_path:
        os.makedirs(full_path, exist_ok=True)


def write_in_file(file_path: str) -> None:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = "\n" if os.path.exists(file_path) else ""

    with open(file_path, "a") as file:
        content += current_date + "\n"

        while True:
            new_line = input("Enter new line of content: ") + "\n"

            if "stop" in new_line:
                break
            else:
                content += new_line

        file.write(content)


def create_file() -> None:
    command = sys.argv

    if len(command) < 3:
        return

    if "-d" in command and "-f" not in command:
        make_dir(command[2:])

    if "-f" in command:
        file_name = command[-1]

        if "-d" not in command:
            write_in_file(file_name)
        else:
            make_dir(command[2:-2])
            write_in_file(os.path.join(*command[2:-2], file_name))


if __name__ == "__main__":
    create_file()
