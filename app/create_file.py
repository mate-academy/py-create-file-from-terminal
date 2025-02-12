import os
from datetime import datetime
from sys import argv


def create_file_from_terminal() -> None:
    dir_names = []
    line_count = 1
    text = ""

    if "-d" in argv:
        dir_names = (
            argv[argv.index("-d") + 1: argv.index("-f")]
            if ("-f" in argv) and (argv.index("-f") > argv.index("-d"))
            else argv[argv.index("-d") + 1:]
        )
        os.makedirs(os.path.join(*dir_names), exist_ok=True)

    if "-f" in argv:
        full_path = os.path.join(
            *dir_names,
            argv[argv.index("-f") + 1]
        )

        if os.path.exists(full_path):
            with open(full_path) as file:
                if file.readline():
                    text += "\n\n"

        text += f"{datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")}\n"

        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            text += f"{line_count} {new_line}\n"
            line_count += 1
        text = text.rstrip("\n")

        with open(full_path, "a") as file:
            file.write(text)


if __name__ == "__main__":
    create_file_from_terminal()
